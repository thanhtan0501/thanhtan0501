#!/usr/bin/env python3
"""Generate honest GitHub commit-time and weekday distributions."""

from __future__ import annotations

import argparse
import datetime as dt
import json
import os
import re
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any
from zoneinfo import ZoneInfo

API_ROOT = "https://api.github.com"
TIMEZONE = ZoneInfo("Asia/Ho_Chi_Minh")
WINDOW_DAYS = 1825
BAR_WIDTH = 28
START_MARKER = "<!-- START_COMMIT_STATS -->"
END_MARKER = "<!-- END_COMMIT_STATS -->"
TIME_HEADING_ICON = "https://github.com/Anmol-Baranwal/Cool-GIFs-For-GitHub/assets/74038190/e012b52a-b326-4c70-962f-91ee5e1c951f"
WEEKDAY_HEADING_ICON = "https://user-images.githubusercontent.com/74038190/212750672-2f3f2b50-c84f-4ed8-a60a-849ae69ff9df.gif"
TIME_BUCKETS = ("Morning", "Daytime", "Evening", "Night")
WEEKDAYS = (
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday",
)


def parse_timestamp(value: str) -> dt.datetime:
    return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))


def classify_time(local_time: dt.datetime) -> str:
    if local_time.hour < 6:
        return "Night"
    if local_time.hour < 12:
        return "Morning"
    if local_time.hour < 18:
        return "Daytime"
    return "Evening"


def is_bot(commit: dict[str, Any]) -> bool:
    author = commit.get("author") or {}
    login = author.get("login") or ""
    return author.get("type") == "Bot" or login.endswith("[bot]")


def summarize_commits(commits: list[dict[str, Any]], username: str) -> dict[str, Any]:
    """Deduplicate and summarize API commit objects for one GitHub user."""
    seen: set[str] = set()
    time_counts = Counter({bucket: 0 for bucket in TIME_BUCKETS})
    weekday_counts = Counter({day: 0 for day in WEEKDAYS})

    for commit in commits:
        sha = commit.get("sha")
        author = commit.get("author") or {}
        if not sha or sha in seen:
            continue
        if author.get("login") != username or is_bot(commit):
            continue
        if len(commit.get("parents") or []) > 1:
            continue

        raw_date = ((commit.get("commit") or {}).get("author") or {}).get("date")
        if not raw_date:
            continue
        local_time = parse_timestamp(raw_date).astimezone(TIMEZONE)
        seen.add(sha)
        time_counts[classify_time(local_time)] += 1
        weekday_counts[local_time.strftime("%A")] += 1

    return {
        "total": len(seen),
        "time": dict(time_counts),
        "weekday": dict(weekday_counts),
    }


def progress_bar(count: int, maximum: int) -> str:
    filled = round((count / maximum) * BAR_WIDTH) if maximum else 0
    return "█" * filled + "░" * (BAR_WIDTH - filled)


def stat_line(label: str, count: int, total: int, maximum: int) -> str:
    percentage = (count / total * 100) if total else 0
    return f"{label:<10} {count:>3} commits  {progress_bar(count, maximum)} {percentage:6.2f} %"


def dominant_label(counts: dict[str, int], fallback: str) -> str:
    maximum = max(counts.values(), default=0)
    if maximum == 0:
        return fallback
    return max(counts, key=lambda label: (counts[label], -list(counts).index(label)))


def render_stats(summary: dict[str, Any]) -> str:
    total = summary["total"]
    time_counts = summary["time"]
    weekday_counts = summary["weekday"]
    time_max = max(time_counts.values(), default=0)
    weekday_max = max(weekday_counts.values(), default=0)
    time_leader = dominant_label(time_counts, "No recent commit pattern")
    weekday_leader = dominant_label(weekday_counts, "No day yet")
    time_emoji = {"Morning": "🌞", "Daytime": "🌆", "Evening": "🌃", "Night": "🌙"}

    lines = [
        START_MARKER,
        (
            f'### <img src="{TIME_HEADING_ICON}" width="28" height="28" '
            f'alt="Day and night animation" /> I\'m Most Active in the '
            f"{time_leader} {time_emoji.get(time_leader, '🦉')}"
        ),
        "",
        "```text",
    ]
    for bucket in TIME_BUCKETS:
        lines.append(stat_line(f"{time_emoji[bucket]} {bucket}", time_counts[bucket], total, time_max))
    lines += [
        "```",
        "",
        (
            f'### <img src="{WEEKDAY_HEADING_ICON}" width="28" height="28" '
            f'alt="Productivity animation" /> I\'m Most Productive on {weekday_leader}'
        ),
        "",
        "```text",
    ]
    for day in WEEKDAYS:
        lines.append(stat_line(day, weekday_counts[day], total, weekday_max))
    lines += ["```", END_MARKER]
    return "\n".join(lines)


def api_json(url: str, token: str | None) -> Any:
    headers = {
        "Accept": "application/vnd.github+json",
        "User-Agent": "thanhtan0501-profile-stats",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    request = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.load(response)


def collect_commits(username: str, token: str | None, now: dt.datetime | None = None) -> list[dict[str, Any]]:
    now = now or dt.datetime.now(dt.timezone.utc)
    since = now - dt.timedelta(days=WINDOW_DAYS)
    repos: list[dict[str, Any]] = []
    page = 1
    while True:
        query = urllib.parse.urlencode({"type": "owner", "per_page": 100, "page": page})
        page_repos = api_json(f"{API_ROOT}/users/{username}/repos?{query}", token)
        if not page_repos:
            break
        repos.extend(page_repos)
        if len(page_repos) < 100:
            break
        page += 1

    commits: list[dict[str, Any]] = []
    eligible = [repo for repo in repos if not repo.get("fork") and not repo.get("archived") and not repo.get("private")]
    for repo in eligible:
        page = 1
        while True:
            query = urllib.parse.urlencode(
                {
                    "author": username,
                    "since": since.isoformat().replace("+00:00", "Z"),
                    "until": now.isoformat().replace("+00:00", "Z"),
                    "per_page": 100,
                    "page": page,
                }
            )
            try:
                page_commits = api_json(f"{API_ROOT}/repos/{username}/{repo['name']}/commits?{query}", token)
            except urllib.error.HTTPError as error:
                if error.code == 409:
                    page_commits = []
                else:
                    raise
            if not page_commits:
                break
            commits.extend(page_commits)
            if len(page_commits) < 100:
                break
            page += 1
    return commits


def replace_generated_block(readme: str, generated: str) -> str:
    pattern = re.compile(re.escape(START_MARKER) + r".*?" + re.escape(END_MARKER), re.DOTALL)
    if not pattern.search(readme):
        raise ValueError("README is missing the commit-stat markers")
    return pattern.sub(generated, readme, count=1)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--username", required=True)
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--token", default=os.environ.get("GITHUB_TOKEN"))
    args = parser.parse_args()

    commits = collect_commits(args.username, args.token)
    summary = summarize_commits(commits, args.username)
    generated = render_stats(summary)
    original = args.readme.read_text(encoding="utf-8")
    updated = replace_generated_block(original, generated)
    if updated != original:
        args.readme.write_text(updated, encoding="utf-8")


if __name__ == "__main__":
    main()
