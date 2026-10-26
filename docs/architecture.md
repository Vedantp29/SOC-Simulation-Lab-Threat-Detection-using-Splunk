# Architecture

![Architecture](../assets/soc-architecture.png)

The diagram shows the **intended design** of the lab. It is not evidence of a deployment.

## Components
| Component | Role | Telemetry |
|---|---|---|
| Windows 10/11 endpoint | Monitored host | Security log, Sysmon, PowerShell test activity |
| Ubuntu endpoint | Monitored host | `auth.log`, `syslog` |
| Kali Linux | Authorized attack simulation | Nmap scan, controlled failed logins; runs a safe PowerShell test **on the Windows lab host** |
| Universal Forwarders | Collection | Read local logs, send to Splunk over TCP 9997 |
| Splunk Enterprise | SIEM | Receive, index, search, alert, dashboard |
| Firewall / network telemetry | Optional source | Connection events for scan detection |
| SOC analyst | Human workflow | Triage, correlation, timeline, IOC, ATT&CK, report |

## Data flows
| # | Path | Label |
|---|---|---|
| 1 | Windows → UF → Splunk | WinEventLog:Security, Sysmon/Operational → `wineventlog`, `sysmon` |
| 2 | Linux → UF → Splunk | auth.log, syslog → `linux` |
| 3 | Network device → Splunk | security events → `firewall` |
| 4 | Authorized test activity → endpoint/network telemetry → Splunk | generated events appear via paths 1–3 |
| 5 | Splunk → Analyst → Investigation → Incident report | searches, alerts, dashboards |

The attack-simulation path is **not** a log path: Kali does not send logs to Splunk directly. Its
activity is observed only through the telemetry the targets and the network generate.

## Index design (proposed)
`wineventlog`, `sysmon`, `linux`, `firewall` — these names are proposals and must be created in
Splunk (see `configs/README.md`). Field names depend on installed add-ons.

## Network design suggestion
Use an isolated host-only or internal virtual network (e.g. `192.168.56.0/24`). Do not bridge the
attack machine to a production or home network.
