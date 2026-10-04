cat > ~/tools/README.md << 'EOF'
# Selwanism

**Personal Pentesting Assistant — A fast, zero-dependency CLI tool for penetration testers.**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux%20%7C%20Windows%20%7C%20macOS-orange)
![Dependencies](https://img.shields.io/badge/Dependencies-Zero-brightgreen)

Selwanism is a lightweight command-line reference that gives you ready-to-use commands for pentesting tasks — from reconnaissance to privilege escalation. It stays in your terminal, works offline, and runs on any system with Python 3.

---

## 📸 Screenshot

![Selwanism CLI](images/screenshot.png)

---

## ✨ Features

- **36+ tools and attack vectors** organized across 9 categories
- **Modular data architecture** — cheatsheets stored in clean, external JSON files
- **Direct CLI execution** — query any tool or keyword directly (`sel nmap`)
- **Dynamic variable substitution** — bind `<IP>`, `<PORT>`, `<URL>` once, use everywhere
- **Zero-dependency clipboard copying** — copy command strings to clipboard
- **Intelligent fuzzy search** — token-based matching when you forget exact names
- **Interactive REPL mode** — shell-like experience with tab-completion
- **Standard packaging** — installable via `pip`, `pipx`, or a simple shell script
- **Works offline** — no internet needed after installation

---

## 🚀 Installation

Choose the method that fits your workflow.

### Method 1 — One-liner (fastest, no sudo)

```bash
mkdir -p ~/selwanism && cd ~/selwanism && \
curl -sL https://raw.githubusercontent.com/salahreds06-selawy/selwanism/main/sel -o sel && \
curl -sL https://raw.githubusercontent.com/salahreds06-selawy/selwanism/main/tools.json -o tools.json && \
chmod +x sel && ./sel
 
Method 2 — Pip / Pipx (recommended for Python users)
pip install git+https://github.com/salahreds06-selawy/selwanism.git
 
Or isolated install:
pipx install git+https://github.com/salahreds06-selawy/selwanism.git
 
Method 3 — Git clone (for developers)
git clone https://github.com/salahreds06-selawy/selwanism.git
cd selwanism
sudo ./install.sh
 
Method 4 — Manual download
 
Download these files from the repository:
• sel
• data/ folder
• selwanism/ folder 
Place them in the same directory, then:
chmod +x sel
./sel
‌⚠️ Important: The sel wrapper and its data/ + selwanism/ folders must always be together. 
 
💻 Usage
 
Interactive mode
sel
 
You get a shell-like prompt where you can type tool names, search, and list everything.
 
One-shot commands
sel nmap             # show all nmap commands
sel sqlmap           # show sqlmap cheatsheet
sel -l               # list every available tool
sel -s recon         # search by tag
sel -s privesc       # privilege escalation tools
sel -h               # full help menu
 
Dynamic variables
 
Inside interactive mode:
sel > set target 10.10.10.10
sel > set port 4444
sel > nmap
 
All commands now auto-fill with your target values.
 
Copy to clipboard
sel nmap -c 1        # copies command #1 to clipboard
 
 
🛠️ Available Tools
Category Tools
Recon nmap, masscan, gobuster, ffuf, dirb, whatweb, subfinder, amass
Web burpsuite, sqlmap, nikto, wpscan, curl
Password hydra, john, hashcat
Exploitation metasploit, msfvenom, searchsploit, reverse_shell
Post-Exploitation linux_privesc, windows_privesc, mimikatz, bloodhound
Active Directory crackmapexec, impacket, responder, enum4linux, smbclient, smbmap
Network wireshark, tcpdump, netcat, socat, ssh, arp_spoofing
Wireless wifi (aircrack-ng)
OSINT osint (theHarvester, Sherlock, ExifTool, WHOIS)

 
 
🧩 Adding Your Own Tools
 
No code changes needed. Just drop a new JSON file in data/tools/:
{
  "mytool": {
    "title": "MyTool - Short Description",
    "tags": ["category1", "category2"],
    "steps": [
      ["Step label", "command to run"],
      ["Another step", "another command"]
    ]
  }
}
 
Save it and the tool appears instantly — in the list, in search, and in interactive mode. 
 
🤝 Contributing
 
Pull requests are welcome. For major changes, please open an issue first so we can discuss what you'd like to change. 
 
📜 License
 
This project is licensed under the MIT License. 
 
👤 Author
 
Salah Eddin Essbihi
• LinkedIn: salah-eddin-essbihi
• TryHackMe: cyber.salah.sec
• GitHub: salahreds06-selawy 
 
🧑‍💻 Contributors
• @salahreds06-selawy — Creator
• @SniperOfTDM — CLI architecture, modular JSON refactor, packaging
