# Screenshots

## Status

The PNGs in this folder named `01-…` to `06-…` are **illustrative mockups** generated for layout
purposes. Each is labelled **"Illustrative UI — replace with actual lab capture"**.
They are **not** screenshots from a running Splunk instance.

## Replace them with genuine captures

After Splunk is installed and the forwarders are sending data:

1. Run the search shown in each mockup (see `detections/` and the main README) in *Search & Reporting*.
2. Set the time range to something visible (e.g. *Last 15 minutes*) and keep the search bar and time picker in frame.
3. Capture the window (Windows: `Win+Shift+S`; macOS: `Cmd+Shift+4`).
4. **Redact** public IPs, real usernames, hostnames you do not want public, licence keys and tokens.
5. Save using the same filename, overwriting the mockup, and commit.
6. Remove the "illustrative" wording from the README section once **all** images are genuine.

| File | Capture |
|---|---|
| `01-index-overview.png` | `\| eventcount summarize=false index=* \| dedup index` |
| `02-live-event-search.png` | Search across the four indexes with timeline visible |
| `03-windows-4625.png` | Failed-logon search (Windows) |
| `04-sysmon-eventid1.png` | Sysmon Event ID 1 table |
| `05-linux-auth.png` | Linux auth events |
| `06-detection-dashboard.png` | Your actual dashboard |
