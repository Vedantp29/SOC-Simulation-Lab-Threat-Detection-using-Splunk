#!/usr/bin/env python3
"""Generate clearly-synthetic key=value events to test SPL *logic* only.

Output is fabricated. It is NOT real telemetry and proves nothing about real
detection performance. Every event carries synthetic=true.

Usage: python3 scripts/generate-synthetic-events.py --out sample-data --seed 42
"""
import argparse, os, random
from datetime import datetime, timedelta

ATTACKER = "192.168.56.50"   # lab Kali address (example)
WIN_HOST, LIN_HOST, FW_HOST = "WIN10-LAB01", "UBUNTU-LAB01", "FW-LAB01"
WIN_IP, LIN_IP = "192.168.56.20", "192.168.56.30"

def ts(t): return t.strftime("%Y-%m-%d %H:%M:%S")

def windows_4625(start, n):
    users = ["labuser", "testadmin", "svc-test"]
    return [f'{ts(start+timedelta(seconds=i*3))} host={WIN_HOST} EventCode=4625 user={random.choice(users)} '
            f'src_ip={ATTACKER} LogonType=3 synthetic=true' for i in range(n)]

def sysmon_1(start):
    rows = [
        ("powershell.exe -NoProfile -EncodedCommand VwByAGkAdABlAC0ATwB1AHQAcAB1AHQAIAAnAFMATwBDAC0ATABBAEIALQBUAEUAUwBUACcA",
         "C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\powershell.exe", "C:\\Windows\\System32\\cmd.exe"),
        ("notepad.exe", "C:\\Windows\\System32\\notepad.exe", "C:\\Windows\\explorer.exe"),
    ]
    out = []
    for i, (cmd, img, parent) in enumerate(rows):
        out.append(f'{ts(start+timedelta(seconds=i*20))} host={WIN_HOST} EventCode=1 User="LAB\\\\labuser" '
                   f'Image="{img}" CommandLine="{cmd}" ParentImage="{parent}" synthetic=true')
    return out

def linux_auth(start, n):
    lines = []
    for i in range(n):
        t = start + timedelta(seconds=i*4)
        lines.append(f'{t.strftime("%b %d %H:%M:%S")} {LIN_HOST} sshd[1234]: Failed password for invalid user '
                     f'testuser from {ATTACKER} port {40000+i} ssh2 synthetic=true')
    t = start + timedelta(seconds=n*4+30)
    lines.append(f'{t.strftime("%b %d %H:%M:%S")} {LIN_HOST} sshd[1240]: Accepted password for labuser from '
                 f'192.168.56.10 port 51000 ssh2 synthetic=true')
    return lines

def firewall(start, n_ports):
    ports = random.sample(range(1, 1024), n_ports)
    out = [f'{ts(start+timedelta(seconds=i))} host={FW_HOST} src_ip={ATTACKER} dest_ip={WIN_IP} '
           f'dest_port={p} action=blocked synthetic=true' for i, p in enumerate(ports)]
    # benign background
    out += [f'{ts(start+timedelta(seconds=i*10))} host={FW_HOST} src_ip=192.168.56.10 dest_ip={LIN_IP} '
            f'dest_port=22 action=allowed synthetic=true' for i in range(3)]
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="sample-data")
    ap.add_argument("--seed", type=int, default=42)
    a = ap.parse_args()
    random.seed(a.seed)
    os.makedirs(a.out, exist_ok=True)
    start = datetime.now().replace(microsecond=0) - timedelta(minutes=30)
    files = {
        "synthetic_windows_4625.log": windows_4625(start, 12),
        "synthetic_sysmon_1.log": sysmon_1(start),
        "synthetic_linux_auth.log": linux_auth(start, 12),
        "synthetic_firewall.log": firewall(start, 20),
    }
    for name, lines in files.items():
        with open(os.path.join(a.out, name), "w") as fh:
            fh.write("\n".join(lines) + "\n")
        print(f"wrote {len(lines):>3} synthetic events -> {os.path.join(a.out, name)}")

if __name__ == "__main__":
    main()
