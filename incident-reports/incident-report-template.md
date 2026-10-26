# Incident Report Template

> Copy this file per case, e.g. `incident-reports/IR-2026-001.md`. Remove guidance text in *italics*.
> Never record real credentials. Redact data you do not want published.

| Field | Value |
|---|---|
| **Incident ID** | IR-YYYY-NNN |
| **Title** | *Short descriptive title* |
| **Severity** | Informational / Low / Medium / High / Critical — *state criteria used* |
| **Status** | Open / Investigating / Contained / Closed — *false positive / benign / true positive* |
| **Detection timestamp** | YYYY-MM-DD HH:MM:SS (timezone) |
| **Detection source** | *Splunk alert / saved search name* |
| **Analyst** | *role or handle only* |

## 1. Summary
*Two or three sentences: what was detected, on which asset, and the current assessment.*

## 2. Source and destination details
| Role | Host | IP | Account | Notes |
|---|---|---|---|---|
| Source | | | | |
| Destination | | | | |

## 3. Relevant event IDs / telemetry
| Index | Event ID / pattern | Meaning | Count |
|---|---|---|---|
| wineventlog | 4625 | Failed logon | |
| wineventlog | 4624 | Successful logon | |
| sysmon | 1 | Process creation | |
| linux | "Failed password" | sshd failed auth | |
| firewall | — | Connection events | |

## 4. Timeline (UTC or stated timezone)
| Time | Source | Event | Significance |
|---|---|---|---|
| | | | |

## 5. Evidence and IOCs
| Type | Value | Source/Search | Context |
|---|---|---|---|
| IP | | | |
| Account | | | |
| Command line | | | |
| File/hash | | | |

*Include the SPL used to obtain each piece of evidence.*

## 6. Analyst observations and confidence
- **Observations:** 
- **Alternative explanations considered:** 
- **Confidence:** Low / Medium / High — *and why*
- **Suspicious activity vs. confirmed compromise:** *state clearly which applies and what evidence would change the conclusion.*

## 7. MITRE ATT&CK mapping
| Tactic | Technique | ID | Evidence |
|---|---|---|---|

## 8. Triage decision
☐ Close – false positive  ☐ Close – benign true positive  ☐ Monitor  ☐ Escalate  ☐ Contain
*Rationale:* 

## 9. Remediation and follow-up
| Action | Owner | Due | Status |
|---|---|---|---|

## 10. Lessons learned / detection tuning
*Threshold changes, new telemetry needed, allow-list entries.*
