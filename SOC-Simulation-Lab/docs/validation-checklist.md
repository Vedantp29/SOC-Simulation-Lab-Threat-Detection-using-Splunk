# Validation Checklist

Tick items only when actually performed. Record dates and short notes. Leave unchecked otherwise.

## Infrastructure
- [ ] Splunk Enterprise installed and Web UI reachable
- [ ] Indexes created: wineventlog, sysmon, linux, firewall
- [ ] Receiving enabled on 9997
- [ ] Windows UF connected (`splunk list forward-server`)
- [ ] Linux UF connected
- [ ] Sysmon installed and running

## Ingestion
- [ ] `index=wineventlog` returns events
- [ ] `index=sysmon` returns Event ID 1
- [ ] `index=linux` returns auth events
- [ ] `index=firewall` returns events (or documented as not configured)
- [ ] Field names confirmed with `| fieldsummary` and queries adjusted

## Detections (test each against real lab data)
- [ ] brute-force.spl variant A (Windows)
- [ ] brute-force.spl variant B (Linux)
- [ ] possible-port-scan.spl
- [ ] suspicious-powershell.spl
- [ ] Thresholds reviewed against a benign baseline
- [ ] False positives noted

## Alerts and reporting
- [ ] Saved searches / alerts created
- [ ] Dashboard created
- [ ] Genuine screenshots captured and redacted
- [ ] Incident report completed from a real lab run

## Evidence log
| Date | Item | Result | Notes |
|---|---|---|---|
|  |  |  |  |
