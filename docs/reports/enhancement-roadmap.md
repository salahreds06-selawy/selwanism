# Selwanism Enhancement Roadmap

## Overview
This roadmap outlines prioritized, actionable engineering enhancements to evolve `selwanism` into a modern pentesting CLI assistant.

---

## Phase 1: Critical CLI Fixes & Compatibility (Immediate Priority)

### 1.1 Non-Interactive CLI Argument Parsing
- Implementation: Integrate Python's standard `argparse` module.
- Behavior:
  - `sel <tool>` (e.g., `sel nmap`): Print cheatsheet directly and exit with code 0.
  - `sel list`: Print all available tools and exit.
  - `sel -h` / `sel --help`: Print standard help and exit.
  - `sel` (no arguments): Launch interactive REPL mode.

### 1.2 Cross-Platform Terminal Compatibility
- Implementation: Replace `os.system('clear')` with platform-aware clearing:
  ```python
  os.system('cls' if os.name == 'nt' else 'clear')
  ```
- Enable ANSI escape sequences on Windows consoles using `colorama` or native `os.system('')`.

### 1.3 Safe Installer Script
- Modify `install.sh` to copy rather than move:
  ```bash
  sudo cp sel /usr/local/bin/sel
  ```

---

## Phase 2: Data Architecture & Modularity

### 2.1 External Cheatsheet Storage
- Separate content from logic by storing tool definitions in JSON or YAML under `data/tools/`:
  - `data/tools/nmap.json`
  - `data/tools/sql_injection.json`
  - `data/tools/active_directory.json`
- Benefits: Contributors can add tools without touching Python logic.

### 2.2 Category and Tag System
- Classify tools into categories:
  - `recon` (nmap, masscan, theHarvester, gobuster)
  - `web` (sqlmap, xss, burp_suite, nikto, wpscan)
  - `privesc` (linux_privesc, windows_privesc, mimikatz)
  - `ad` (bloodhound, mimikatz, kerberoast, secretsdump)
  - `wireless` (aircrack-ng, bettercap)
  - `pivoting` (chisel, ligolo-ng, socat)

---

## Phase 3: Interactive Features & Pentester UX

### 3.1 Target Variable Substitution
- Allow setting target variables inside the interactive session:
  - `set target 10.10.10.10`
  - `set port 4444`
  - `set url http://target.local`
- Dynamic rendering: Automatically replaces `<IP>`, `<PORT>`, `<URL>` in displayed commands.

### 3.2 Command Copy to Clipboard
- Add optional flag or shortcut to copy a command:
  - `sel nmap -c 2` (copies command #2 to system clipboard)

### 3.3 Enhanced Fuzzy Search
- Implement token-based or fuzzy matching for quick discovery when exact tool names are forgotten.

---

## Phase 4: Pentesting Content Expansion

### 4.1 Modern Active Directory Techniques
- Kerberoasting (`impacket-GetUserSPNs`)
- AS-REP Roasting (`impacket-GetNPUsers`)
- Active Directory Certificate Services (AD CS / Certipy)
- DCSync and secretsdump

### 4.2 Modern Web & API Exploitation
- Fuzzing with `ffuf` and `feroxbuster`
- Server-Side Request Forgery (SSRF)
- JSON Web Token (JWT) attacks
- Cross-Site WebSocket Hijacking

### 4.3 Pivoting & Tunneling
- Chisel SOCKS5 reverse proxy
- Ligolo-ng tun interface setup
- SSH local and dynamic forwarding

---

## Phase 5: Packaging & Distribution

### 5.1 Python Packaging Standards
- Introduce `pyproject.toml` using `setuptools` or `hatchling`.
- Expose entrypoint `sel = selwanism.cli:main`.
- Support installation via `pipx install git+https://github.com/salahreds06-selawy/selwanism.git`.

### 5.2 Automated Testing
- Add `tests/` directory with `pytest`.
- Validate argument parsing, data loading integrity, and search query precision.
