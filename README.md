# Selwanism

Personal Pentesting Assistant — A fast, zero-dependency CLI tool for penetration testers.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-orange)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)

## What is Selwanism?

Selwanism is a lightweight command-line assistant that provides ready-to-use commands, penetration testing techniques, and step-by-step guides for red teaming and security assessments. It covers reconnaissance, web application security, privilege escalation, Active Directory exploitation, network pivoting, and hash cracking.

No mandatory third-party dependencies. No internet connection required. Pure Python.

---

## Features

- **36 Tools & Attack Vectors** organized across 9 distinct categories.
- **Modular Data Architecture**: cheatsheets stored in clean, external JSON files under `data/tools/`.
- **Direct CLI Execution**: query any tool or keyword directly (`sel nmap`, `sel sql`, `sel privesc`).
- **Dynamic Variable Substitution**: bind `-t <IP>`, `-p <PORT>`, and `-u <URL>` to populate placeholders in all commands.
- **Zero-Dependency Clipboard Copying**: copy command strings directly to the clipboard with `-c <NUM>` (supports native OS utilities with optional `pyperclip` fallback).
- **Intelligent Fuzzy Search**: token-based and character-similarity search for discovery even with typos (`sel nmapp`, `sel cert`, `sel tunnel`).
- **Interactive REPL Mode**: interactive session with variable state management, command copy shortcuts, and terminal clearing.
- **Standard Packaging**: installable via `pip`, `pipx`, or as a standalone executable.

---

## Installation

### Via Pip / Pipx
```bash
# Direct install from repository
pip install .

# Or with optional pyperclip support
pip install ".[clipboard]"

# Isolated global CLI install via pipx
pipx install git+https://github.com/salahreds06-selawy/selwanism.git
```

### Linux & macOS (Native Script)
```bash
git clone https://github.com/salahreds06-selawy/selwanism.git
cd selwanism
sudo ./install.sh
```

### Windows
Run directly with Python 3:
```powershell
python sel nmap
python sel -t 10.10.10.50 -c 2 nmap
```

---

## Usage

### Direct CLI Commands
```bash
first:    --sel--                 # for a better interface
sel -h                            # Display help menu
sel list                          # Display all 36 tools grouped by category
sel nmap                          # View Nmap scanner commands
sel nmap -t 10.10.10.50           # View Nmap commands with IP substituted
sel nmap -t 10.10.10.50 -c 2      # Copy command #2 directly to clipboard
sel chisel                        # View network pivoting and SOCKS5 steps
sel ligolo_ng                     # View Ligolo-ng transparent pivoting
sel adcs                          # Active Directory Certificate Services attacks
sel ssrf                          # Server-Side Request Forgery metadata endpoints
sel jwt_attacks                   # JWT brute-forcing and token manipulation
sel privesc                       # Search Linux & Windows privilege escalation
sel nmapp                         # Fuzzy search matches 'nmap'
```

### Interactive REPL Mode
Run `sel` with no arguments to start the interactive session:
```text
sel > set target 10.10.10.50
[+] target set to: 10.10.10.50

sel > set port 8080
[+] port set to: 8080

sel[10.10.10.50:p:8080] > nmap
  ┌──────────────────────────────────────────────────────────────────────┐
  │ Nmap - Network Scanner                                               │
  │ Category: Reconnaissance                                             │
  │ Discover hosts and services on a network.                            │
  │ Bound: target=10.10.10.50, port=8080                                 │
  └──────────────────────────────────────────────────────────────────────┘

    [01] Quick scan
         $ nmap -sV 10.10.10.50

    [02] Full TCP scan
         $ nmap -sV -sC -p- -T4 10.10.10.50

sel[10.10.10.50:p:8080] > copy nmap 2
[+] Successfully copied command [02] to clipboard!

sel[10.10.10.50:p:8080] > vars
Current Active Variables:
  Target IP: 10.10.10.50
  Port:      8080
  URL:       None
  LHOST:     None

sel[10.10.10.50:p:8080] > exit
```

---

## Tool Categories (36 Tools)

- **Reconnaissance (4)**: Nmap, Gobuster, OSINT, Masscan
- **Web Application (10)**: SQL Injection, XSS, IDOR, FFUF, Burp Suite, Nikto, WPScan, SSRF, JWT Attacks, WebSocket Hijacking (CSWSH)
- **Privilege Escalation (3)**: Linux PrivEsc, Windows PrivEsc, PowerShell Post-Exploitation
- **Active Directory (8)**: BloodHound, Mimikatz, Kerberoasting, AS-REP Roasting, AD CS (Certipy), secretsdump, Enum4linux, SMBClient
- **Pivoting & Tunneling (3)**: Chisel, Ligolo-ng, SSH Port Forwarding
- **Exploitation & Shells (2)**: Reverse Shells, Metasploit Framework
- **Password Cracking (3)**: Hydra, John the Ripper, Hashcat
- **Network & MITM (2)**: ARP Spoofing (Bettercap), Wireshark
- **Wireless Attacks (1)**: WiFi Hacking (Aircrack-ng)

---

## Data Architecture

Cheatsheet definitions live in `data/tools/*.json`. To add a new tool or category, add or edit a JSON file:

```json
{
  "my_tool": {
    "title": "My Tool Title",
    "category": "Reconnaissance",
    "desc": "Tool description here.",
    "steps": [
      ["Scan target", "mytool -t <IP> -p <PORT>"]
    ]
  }
}
```

---

## License

MIT License.

## Author

**Salah Eddin Essbihi**
- LinkedIn: salah-eddin-essbihi
- TryHackMe: cyber.salah.sec---

## 🧑‍💻 Contributors

- [@salahreds06-selawy](https://github.com/salahreds06-selawy) — Creator
- [@SniperOfTDM](https://github.com/SniperOfTDM) — CLI architecture, modular JSON refactor, packaging
- GitHub: salahreds06-selawy
