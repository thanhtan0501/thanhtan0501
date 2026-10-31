#!/usr/bin/env python3
import datetime as dt

from update_commit_stats import render_stats, summarize_commits


def fake_commit(sha, timestamp, login="thanhtan0501", parents=None, author_type="User"):
    return {
        "sha": sha,
        "author": {"login": login, "type": author_type},
        "parents": [{"sha": parent} for parent in (parents or ["parent"])],
        "commit": {"author": {"date": timestamp}},
    }


def main():
    commits = [
        fake_commit("morning", "2026-01-01T00:00:00Z"),  # 07:00 local
        fake_commit("daytime", "2026-01-01T06:00:00Z"),  # 13:00 local
        fake_commit("evening", "2026-01-01T12:00:00Z"),  # 19:00 local
        fake_commit("night", "2026-01-01T17:00:00Z"),  # 00:00 local next day
        fake_commit("duplicate", "2026-01-02T06:00:00Z"),
        fake_commit("duplicate", "2026-01-02T06:00:00Z"),
        fake_commit("merge", "2026-01-03T06:00:00Z", parents=["a", "b"]),
        fake_commit("bot", "2026-01-04T06:00:00Z", login="dependabot[bot]", author_type="Bot"),
        fake_commit("other-user", "2026-01-05T06:00:00Z", login="someone-else"),
    ]
    summary = summarize_commits(commits, "thanhtan0501")
    assert summary["total"] == 5
    assert summary["time"] == {"Morning": 1, "Daytime": 2, "Evening": 1, "Night": 1}
    assert summary["weekday"] == {
        "Monday": 0,
        "Tuesday": 0,
        "Wednesday": 0,
        "Thursday": 3,
        "Friday": 2,
        "Saturday": 0,
        "Sunday": 0,
    }
    rendered = render_stats(summary)
    assert "I'm Most Active in the Daytime" in rendered
    assert "I'm Most Productive on Thursday" in rendered
    assert "START_COMMIT_STATS" in rendered and "END_COMMIT_STATS" in rendered
    print("commit stats tests: passed")


if __name__ == "__main__":
    main()
