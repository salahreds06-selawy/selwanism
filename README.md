# Selwanism

**Personal Pentesting Assistant — A CLI tool for penetration testers.**

![Python](https://img.shields.io/badge/Python-3.x-blue)
![License](https://img.shields.io/badge/License-MIT-green)
![Platform](https://img.shields.io/badge/Platform-Linux-orange)
![Version](https://img.shields.io/badge/Version-2.0-red)

Selwanism is a lightweight command-line reference that gives you ready-to-use commands for pentesting tasks — from reconnaissance to privilege escalation. It stays in your terminal, works offline, and needs only Python 3.

---


## ✨ Features

- **50+ tools and attack techniques** across recon, web, AD, privesc, network, and more
- **Smart search** by name, title, or tag (`sel -s recon`, `sel -s privesc`)
- **Zero dependencies** — works with just Python 3
- **Offline** — no internet required after installation
- **Easy to extend** — add tools by editing a single JSON file
- **Colored CLI interface** with a clean, readable layout
- **Interactive mode** — just type `sel`

---

## 🚀 Installation

Choose the method that fits your workflow.

### Method 1 — One-liner (fastest, no `sudo`)

Copies Selwanism into `~/selwanism` and runs it immediately:

```bash
mkdir -p ~/selwanism && cd ~/selwanism && \
curl -sL https://raw.githubusercontent.com/salahreds06-selawy/selwanism/main/sel -o sel && \
curl -sL https://raw.githubusercontent.com/salahreds06-selawy/selwanism/main/tools.json -o tools.json && \
chmod +x sel && ./sel
 
Method 2 — Install globally (recommended)
 
Installs sel into /usr/local/bin so you can run it from any directory:
sudo curl -sL https://raw.githubusercontent.com/salahreds06-selawy/selwanism/main/sel -o /usr/local/bin/sel && \
sudo curl -sL https://raw.githubusercontent.com/salahreds06-selawy/selwanism/main/tools.json -o /usr/local/bin/tools.json && \
sudo chmod +x /usr/local/bin/sel
 
Then simply run:
sel
 
Method 3 — Git clone (for developers)
git clone https://github.com/salahreds06-selawy/selwanism.git
cd selwanism
chmod +x sel
./sel
 
Method 4 — Manual download
 
Download these two files manually from the repository:
• sel
• tools.json 
Place them in the same folder, then:
chmod +x sel
./sel
‌⚠️ Important: sel and tools.json must always be in the same directory. sel reads its data from tools.json. 
 
💻 Usage
 
Interactive mode
 
Just run:
sel
 
You'll get a shell-like prompt where you can type tool names, search, and list everything.
 
One-shot commands
sel nmap             # show all nmap commands
sel sqlmap           # show sqlmap cheatsheet
sel -l               # list every available tool
sel -s recon         # search by tag
sel -s privesc       # privilege escalation tools
sel -h               # full help menu
 
Examples
$ sel nmap

  Nmap - Network Scanner
  ----------------------

  [1] Quick scan
      $ nmap -sV <IP>
  [2] Full TCP scan
      $ nmap -sV -sC -p- -T4 <IP>
  [3] UDP scan
      $ nmap -sU --top-ports 100 <IP>
  ...
 
 
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
 
No code changes needed. Just edit tools.json:
"mytool": {
  "title": "MyTool - Short Description",
  "tags": ["category1", "category2"],
  "steps": [
    ["Step label", "command to run"],
    ["Another step", "another command"]
  ]
}
 
Save the file and the tool appears instantly — in the list, in search, and in interactive mode. 
 
🤝 Contributing
 
Pull requests are welcome. For major changes, please open an issue first so we can discuss what you'd like to change. 
 
📜 License
 
This project is licensed under the MIT License. 
 
👤 Author
 
Salah Eddin Essbihi
• LinkedIn: salah-eddin-essbihi
• TryHackMe: cyber.salah.sec
• GitHub: salahreds06-selawy
