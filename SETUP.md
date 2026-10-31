# Profile README setup

This folder is the published profile repository for [`thanhtan0501/thanhtan0501`](https://github.com/thanhtan0501/thanhtan0501).

## Publish or update

The repository is public and uses the `main` branch. Keep `README.md` at the repository root and `assets/hero.svg` in `assets/`, then commit and push updates to `main`.

## Commit statistics

`.github/workflows/update-readme-stats.yml` runs every Monday at 02:17 UTC and supports `workflow_dispatch` for manual refreshes. It uses only the repository's built-in `GITHUB_TOKEN` with `contents: write` permission.

The generator in `scripts/update_commit_stats.py`:

- Reads public, owned, non-fork, non-archived repositories for `thanhtan0501`.
- Uses the rolling five-year window ending at workflow execution time.
- Includes commits whose GitHub API `author.login` is exactly `thanhtan0501`.
- Deduplicates commit SHAs, excludes merge commits, and excludes bot authors.
- Converts Git author timestamps to `Asia/Ho_Chi_Minh` (UTC+07:00).
- Updates only the `START_COMMIT_STATS` / `END_COMMIT_STATS` block.
- Leaves the README unchanged when the generated block is unchanged.

Run the local regression check with:

```bash
python3 scripts/test_commit_stats.py
```

No WakaTime account or token is needed. `anmol098/waka-readme-stats` was reviewed as a reference, but a small standard-library generator is narrower and avoids unrelated personal metrics.

## Native GitHub Activity overview

The four-axis Activity overview is a GitHub profile setting, not README content. GitHub documents enabling it from the profile's **Contribution settings → Activity overview** menu. The available browser session could not provide an authenticated GitHub UI session for this account, and GitHub exposes no supported CLI/API mutation for this setting. Enable it manually if desired; this does not change repository data or private-contribution visibility.

## External services and assets

- `skillicons.dev` renders grouped technology icons.
- `img.shields.io` renders small technology and profile badges.
- `komarev.com/ghpvc` renders the profile-view counter.
- `streak-stats.demolab.com` renders the contribution-streak card.
- `readme-jokes.vercel.app` renders the random programming joke SVG.
- The small GIFs are hotlinked from [TheDudeThatCode/TheDudeThatCode](https://github.com/TheDudeThatCode/TheDudeThatCode) and are not copied into this repository. The source repository did not expose license metadata during audit, so replace those URLs with approved/original assets if redistribution rights are required.

The local `assets/hero.svg` is original to this profile composition and has no third-party asset dependency.

## Content and ownership notes

The featured projects are public, non-fork repositories verified through the GitHub API. The newer skill repositories are forks and are intentionally not presented as original work. No employer, credentials, private repository, client information, or unverified social URL is included.

The quote is a static, attributed Leslie Lamport quote; no quote-rotation action or secret is required.

## Reference patterns studied

- [sciencepal/sciencepal](https://github.com/sciencepal/sciencepal): playful animated greeting, visitor counter, and dashboard-like activity blocks.
- [apoorvtyagi/apoorvtyagi](https://github.com/apoorvtyagi/apoorvtyagi): compact animated headings, structured About Me, grouped skills, streak/activity sections, quote, and humour card.

This README borrows those composition ideas without copying their biographies, personal URLs, or statistics.
