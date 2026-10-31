# Profile README setup

This folder is the published profile repository for [`thanhtan0501/thanhtan0501`](https://github.com/thanhtan0501/thanhtan0501).

## Publish or update

The repository is public and uses the `main` branch. Keep `README.md` at the repository root and the local hero at `assets/footer.webp`, then commit and push updates to `main`.

The hero is a local copy of the exact static 2000×400 WebP from [Aurorp1g/Aurorp1g](https://github.com/Aurorp1g/Aurorp1g). Its SHA-256 is `574f20aac46633476c6bb029203c98555b5bf7f81210fa69429ec287c9a0b825`. The source repository did not expose license metadata during audit, so the file is retained with that source attribution but should be replaced or removed if reuse permission is not confirmed.

The Skills block is one unified, five-column icon gallery rather than a categorized table. Animated icons are hotlinked from [qkrdmstlr3/techstack-generator](https://github.com/qkrdmstlr3/techstack-generator), static icons from [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons) and Simple Icons, and conceptual skills use neutral Shields badges. The referenced icon repositories expose MIT licenses.

## Commit statistics

`.github/workflows/update-readme-stats.yml` runs every Monday at 02:17 UTC and supports `workflow_dispatch` for manual refreshes. It uses only the repository's built-in `GITHUB_TOKEN` with `contents: write` permission.

The workflow has a repository-level concurrency group so a scheduled run and a manual run cannot commit competing README versions at the same time. It updates only the `START_COMMIT_STATS` / `END_COMMIT_STATS` block, leaving the Skills, summary cards, hero, links, quote, and humour sections untouched.

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

## GitHub Profile Summary Card

The README uses only the hosted profile-details/contribution timeline card from [`vn7n24fzkq/github-profile-summary-cards`](https://github.com/vn7n24fzkq/github-profile-summary-cards):

- Username is fixed to `thanhtan0501`.
- Theme is `default` with `animation=none`.
- The card is a read-only hosted SVG, so it does not add another workflow, token, generated directory, or README writer.
- The endpoint returned HTTP 200 with `image/svg+xml` content and the expected username/theme markers during the v3 audit.

The hosted card and the custom commit-distribution block intentionally use different data sources and counting rules. Their totals should not be expected to match.

## Native GitHub Activity overview

The four-axis Activity overview is a GitHub profile setting, not README content. To enable it:

1. Open `https://github.com/thanhtan0501`.
2. Scroll to the contribution graph.
3. Click **Contribution settings**.
4. Enable **Activity overview**.
5. Refresh the profile page.

The available browser session could not provide an authenticated GitHub UI session for this account, and GitHub exposes no supported CLI/API mutation for this setting. Do not change unrelated contribution privacy settings.

## External services and assets

- `skillicons.dev` renders the static technology icons in the unified Skills gallery.
- `techstack-generator.vercel.app` renders the animated technology SVGs in the unified Skills gallery.
- `cdn.simpleicons.org` renders the white WebSockets and Drizzle icons used for dark-mode contrast.
- `img.shields.io` renders small technology and profile badges.
- `komarev.com/ghpvc` renders the profile-view counter.
- `streak-stats.demolab.com` renders the neutral/default contribution-streak card.
- `readme-jokes.vercel.app` renders the random programming joke SVG with its basic light theme.
- `github-profile-summary-cards.vercel.app` renders only the neutral/default profile-details card.
- The small GIFs are hotlinked from [TheDudeThatCode/TheDudeThatCode](https://github.com/TheDudeThatCode/TheDudeThatCode) and are not copied into this repository. The source repository did not expose license metadata during audit, so replace those URLs with approved/original assets if redistribution rights are required.
- The handshake GIF is hotlinked from [ashu-guo/ashu-guo](https://github.com/ashu-guo/ashu-guo), whose repository exposes an MIT license. It is not copied into this repository.
- The LinkedIn icon is from [tandpfun/skill-icons](https://github.com/tandpfun/skill-icons), and the Instagram icon is from the [github-profile-readme-generator](https://github.com/rahuldkjain/github-profile-readme-generator) asset collection. They are hotlinked, not copied.
- `assets/footer.webp` is the locally hosted hero image; the previous `assets/hero.svg` was removed because it was no longer referenced.

## Content and ownership notes

No employer, credentials, private repository, client information, or unverified social URL is included.

The quote is a static, attributed Leslie Lamport quote; no quote-rotation action or secret is required.

## Reference patterns studied

- [sciencepal/sciencepal](https://github.com/sciencepal/sciencepal): playful animated greeting, visitor counter, and dashboard-like activity blocks.
- [apoorvtyagi/apoorvtyagi](https://github.com/apoorvtyagi/apoorvtyagi): compact animated headings, structured About Me, streak/activity sections, quote, and humour card.
- [suraweera-AGSS/suraweera-AGSS](https://github.com/suraweera-AGSS/suraweera-AGSS): compact icon gallery and contact presentation.

This README borrows those composition ideas without copying their biographies, personal URLs, or statistics.
