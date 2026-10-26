# ⚠ SIMULATED — NOT A REAL INCIDENT

> This is a **fictional training scenario** written to demonstrate the report format.
> All hosts, accounts, IP addresses, times and counts are **invented placeholders** (private lab
> ranges). Nothing here was measured from a real system or deployed Splunk instance.
> Replace with findings from your own authorized lab runs.

| Field | Value |
|---|---|
| **Incident ID** | SIM-001 |
| **Title** | Repeated failed logons followed by a successful logon (training scenario) |
| **Severity** | Medium *(criteria: multiple failures + later success on one lab host)* |
| **Status** | Closed — expected lab activity (authorized test) |
| **Detection timestamp** | 2026-01-01 10:15 (fictional) |
| **Detection source** | `detections/brute-force.spl` — variants A and C |

## 1. Summary
A scheduled search flagged many failed Windows logons (Event ID 4625) from one lab address against
three accounts on `WIN10-LAB01`, followed by one successful logon (4624). In this scenario, the
source is the lab's Kali machine running a controlled failed-login test.

## 2. Source and destination
| Role | Host | IP | Account | Notes |
|---|---|---|---|---|
| Source | kali-lab | 192.168.56.50 | — | Authorized attack-simulation machine |
| Destination | WIN10-LAB01 | 192.168.56.20 | labuser, testadmin, svc-test | Lab endpoint |

## 3. Relevant events
| Index | Event | Meaning |
|---|---|---|
| wineventlog | 4625 | Failed logon (fictional count: 12) |
| wineventlog | 4624 | Successful logon (fictional count: 1) |

## 4. Timeline (fictional)
| Time | Event | Significance |
|---|---|---|
| 10:10:00 | Test begins from 192.168.56.50 | Matches lab test plan |
| 10:10:00–10:10:36 | 12 × 4625 across 3 accounts | Exceeds threshold (≥10 / 5 min) |
| 10:11:10 | 1 × 4624 from same source | Success after failures — raises priority |
| 10:15:00 | Alert fires | Triage begins |

## 5. Evidence / IOCs
| Type | Value | Context |
|---|---|---|
| IP | 192.168.56.50 | Internal lab host (documented test machine) |
| Accounts | labuser, testadmin, svc-test | Lab accounts only |

## 6. Analyst observations and confidence
- Source IP matches the documented attack-simulation host and the test window in the lab log.
- No unexpected process creation on the host (would check Sysmon Event ID 1).
- **Assessment:** suspicious pattern, explained by authorized testing. **Not** a confirmed compromise.
- **Confidence:** High (known test) — would be *Low* if the source were unknown.

## 7. ATT&CK mapping
| Tactic | Technique | ID |
|---|---|---|
| Credential Access | Brute Force | T1110 |

## 8. Triage decision
Close as authorized test. If the source had been unrecognised: escalate, review 4624 session, reset
affected credentials, review Sysmon activity after the success.

## 9. Remediation / follow-up (illustrative)
| Action | Status |
|---|---|
| Add lab-test window annotation to alert notes | Proposed |
| Consider account lockout policy (lab) | Proposed |
| Tune threshold after baseline review | Proposed |
