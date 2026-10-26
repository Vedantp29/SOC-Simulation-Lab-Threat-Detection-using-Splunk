# Contributing

This project is built by two contributors in one shared repository. Follow this workflow so history stays clear and every change is reviewed.

## Workflow
1. **Pull the latest `main`** before starting: `git checkout main && git pull`.
2. **Create a branch** for one task: `git checkout -b detections-brute-force`.
   Suggested names: `detections-*`, `docs-*`, `configs-*`, `screenshots-*`, `incident-*`.
3. **Commit small, clear changes** under your own GitHub account.
   Example: `Add Linux sshd variant to brute-force detection`.
4. **Push and open a pull request** into `main`: `git push -u origin <branch>`.
5. **The other contributor reviews** and approves. Do not merge your own PR without a review.
6. **Delete the branch** after merging.

Optional: in *Settings → Branches*, add a rule for `main` that requires a pull request before merging.

## Rules for content
- **Only claim what was done.** Tick `docs/validation-checklist.md` boxes only after testing. Keep SPL marked DRAFT until validated against real data.
- **Label mock content.** Illustrative images stay labelled until replaced by real captures.
- **No secrets or personal data.** Never commit passwords, keys, license files, or real logs. Redact public IPs, usernames, and hostnames in screenshots.
- **Keep files consistent.** Index names (`wineventlog`, `sysmon`, `linux`, `firewall`), field names, and ATT&CK IDs must match across README, detections, and docs.
- **Safe testing only.** Authorized, isolated lab systems; benign test activity.

## Detection changes
Include in the PR description: what the detection looks for, telemetry/index used, how you tested it, and any false positives seen.

## Suggested ownership
Record who owns which area in the README's Contributors section. Review each other's work regardless of ownership.
