# Configuration Examples

> **Status: examples only — not yet tested in a deployed lab.** Paths, ports, add-on names and
> sourcetypes vary by version. Validate each item against the official Splunk documentation
> and with `splunk btool` / `splunk list monitor` before relying on it.

Copy these into the relevant `local/` directories (never edit `default/`). Do **not** commit real
hostnames, passwords or certificates.

## 1. Splunk Enterprise — create indexes (`$SPLUNK_HOME/etc/system/local/indexes.conf`)

```ini
[wineventlog]
homePath   = $SPLUNK_DB/wineventlog/db
coldPath   = $SPLUNK_DB/wineventlog/colddb
thawedPath = $SPLUNK_DB/wineventlog/thaweddb

[sysmon]
homePath   = $SPLUNK_DB/sysmon/db
coldPath   = $SPLUNK_DB/sysmon/colddb
thawedPath = $SPLUNK_DB/sysmon/thaweddb

[linux]
homePath   = $SPLUNK_DB/linux/db
coldPath   = $SPLUNK_DB/linux/colddb
thawedPath = $SPLUNK_DB/linux/thaweddb

[firewall]
homePath   = $SPLUNK_DB/firewall/db
coldPath   = $SPLUNK_DB/firewall/colddb
thawedPath = $SPLUNK_DB/firewall/thaweddb
```

Or use **Settings → Indexes → New Index** in Splunk Web.

## 2. Splunk Enterprise — enable receiving

Settings → Forwarding and receiving → Configure receiving → New receiving port → `9997`
(or `splunk enable listen 9997`).

## 3. Windows Universal Forwarder — `inputs.conf`

```ini
[WinEventLog://Security]
index = wineventlog
disabled = 0
renderXml = false

[WinEventLog://Microsoft-Windows-Sysmon/Operational]
index = sysmon
disabled = 0
renderXml = true
source = XmlWinEventLog:Microsoft-Windows-Sysmon/Operational
```

Install **Sysmon** with a reviewed community or custom configuration (e.g. SwiftOnSecurity or
Olaf Hartong's sysmon-modular — review before use) and the **Splunk Add-on for Sysmon** /
**Splunk Add-on for Microsoft Windows** on the search head for field extraction.

## 4. Linux Universal Forwarder — `inputs.conf`

```ini
[monitor:///var/log/auth.log]
index = linux
sourcetype = linux_secure
disabled = 0

[monitor:///var/log/syslog]
index = linux
sourcetype = syslog
disabled = 0
```

(On RHEL-family systems, use `/var/log/secure` and `/var/log/messages`.) The forwarder user must
have read permission on these files.

## 5. Both forwarders — `outputs.conf`

```ini
[tcpout]
defaultGroup = lab_splunk

[tcpout:lab_splunk]
server = <SPLUNK_SERVER_IP>:9997
```

## 6. Verify

```bash
# On the forwarder
splunk list forward-server
splunk list monitor
# In Splunk Search
| eventcount summarize=false index=* | dedup index | fields index count
index=_internal host=<forwarder-host> | head 5
```
