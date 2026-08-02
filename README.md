# VaranasiCountdown

Tweets a daily countdown of days remaining until 2026-04-07, posted around 9 PM IST.

## Scheduling via cron-job.org

This repo previously relied on GitHub Actions' native `schedule` trigger, which
GitHub automatically disables after 60 days without repository activity — hence
the old daily "keepalive" empty-commit hack. That's been replaced with an
external trigger from [cron-job.org](https://cron-job.org), which fires a
`repository_dispatch` event instead. `repository_dispatch` (unlike `schedule`)
is never auto-disabled, so no keepalive commits are needed.

To wire it up:

1. Create a GitHub [personal access token](https://github.com/settings/tokens)
   with `repo` scope (classic) or `Contents: read/write` + `Actions: read/write`
   (fine-grained), scoped to this repository.
2. In cron-job.org, create a new cron job:
   - **URL:** `https://api.github.com/repos/pj-18/varanasicountdown/dispatches`
   - **Schedule:** daily at `15:10 UTC` (matches the original workflow schedule)
   - **Request method:** `POST`
   - **Headers:**
     - `Accept: application/vnd.github+json`
     - `Authorization: Bearer <YOUR_GITHUB_TOKEN>`
     - `Content-Type: application/json`
   - **Body:**
     ```json
     {"event_type": "cron-tweet"}
     ```
3. Save and enable the job. Each firing triggers
   `.github/workflows/schedule-tweet.yml`, which runs `tweet.py`.

The workflow can still be run manually from the Actions tab via
`workflow_dispatch`.
