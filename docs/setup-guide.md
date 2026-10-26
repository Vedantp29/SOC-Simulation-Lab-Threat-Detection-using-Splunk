# Setup Guide

> Procedure outline. Nothing here asserts the lab has been built. Check official docs for current versions.

## 0. Safety rules
- Test **only** systems you own, inside an isolated virtual network.
- Snapshot every VM before testing.
- Keep Kali off any production/home LAN. Do not attack third-party hosts.
- PowerShell tests must be benign (see §6). No malware, no real credentials, no exploitation.

## 1. VMs
| VM | Suggested OS | Notes |
|---|---|---|
| splunk-server | Ubuntu Server or Windows | 4+ GB RAM recommended |
| win10-lab | Windows 10/11 | Test accounts only |
| ubuntu-lab | Ubuntu | OpenSSH server for auth log events |
| kali-lab | Kali Linux | Attack simulation |

Network: one host-only/internal network, static IPs (example `192.168.56.0/24`).

## 2. Splunk Enterprise
1. Install Splunk Enterprise (free trial/dev licence per Splunk terms).
2. Create indexes `wineventlog`, `sysmon`, `linux`, `firewall` (`configs/README.md` §1).
3. Enable receiving on 9997.
4. Install add-ons for field extraction (Splunk Add-on for Microsoft Windows, for Sysmon, for Unix and Linux).

## 3. Windows endpoint
1. Install Sysmon with a reviewed config.
2. Enable auditing for logon events (Local Security Policy → Audit Logon: success + failure).
3. Install Universal Forwarder; configure `inputs.conf`, `outputs.conf` (`configs/README.md` §3, §5).
4. Optional: enable PowerShell Script Block Logging (4104) and collect it.

## 4. Linux endpoint
1. Install `openssh-server`.
2. Install Universal Forwarder; configure monitors (`configs/README.md` §4).

## 5. Verify ingestion
Run the verification searches in `configs/README.md` §6 and complete `docs/validation-checklist.md`.

## 6. Controlled test activity (authorized lab only)

**Failed logons (Windows):** attempt a handful of incorrect logons for lab accounts (e.g. via RDP/SMB
from kali-lab or interactively). Use 10–15 attempts at lab-created accounts only.

**Failed logons (Linux):** make several wrong SSH password attempts against `ubuntu-lab`.

**Port scan:** from kali-lab against `win10-lab` only:
```bash
nmap -sT -p 1-100 192.168.56.20
```
Requires firewall/network telemetry for `index=firewall`. Windows Firewall logging can be used if
configured and ingested; field names will then need mapping to `src_ip`, `dest_ip`, `dest_port`.

**Benign PowerShell test (run on win10-lab):**
```powershell
powershell.exe -NoProfile -EncodedCommand VwByAGkAdABlAC0ATwB1AHQAcAB1AHQAIAAnAFMATwBDAC0ATABBAEIALQBUAEUAUwBUACcA
```
This decodes to `Write-Output 'SOC-LAB-TEST'` and only prints a string, but its form triggers the
`-EncodedCommand` pattern.

## 7. Evidence capture
Follow `assets/screenshots/README.md` to replace the illustrative mockups.
