#!/usr/bin/env python3
# ============================================
#   SELWANISM - Personal Pentesting Assistant
#   Author: Salah Eddin Essbihi
#   Version: 2.1.0
# ============================================

import os
import sys
import json
import argparse
import difflib
import subprocess

# ====== ANSI Color Codes ======
RED = '\033[91m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'
GRAY = '\033[90m'
BOLD = '\033[1m'
RESET = '\033[0m'

def enable_vt_mode():
    """Enable UTF-8 stdout and ANSI VT processing on Windows."""
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')
    if os.name == 'nt':
        try:
            import ctypes
            kernel32 = ctypes.windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
        except Exception:
            os.system('')

def clear_screen():
    """Clear terminal screen cross-platform."""
    os.system('cls' if os.name == 'nt' else 'clear')

# ====== Data Loader ======
def load_tools():
    """Load tool cheatsheets from external JSON files across candidate directories."""
    tools = {}
    base_dir = os.path.dirname(os.path.abspath(__file__))
    
    candidate_dirs = [
        os.path.join(base_dir, "data", "tools"),
        os.path.join(base_dir, "..", "data", "tools"),
        os.path.join(os.getcwd(), "data", "tools"),
        "/usr/share/selwanism/data/tools",
        os.path.expanduser("~/.local/share/selwanism/data/tools")
    ]
    
    seen_dirs = set()
    for cdir in candidate_dirs:
        norm_dir = os.path.normpath(cdir)
        if norm_dir in seen_dirs or not os.path.isdir(norm_dir):
            continue
        seen_dirs.add(norm_dir)
        try:
            for fname in sorted(os.listdir(norm_dir)):
                if fname.endswith(".json"):
                    fpath = os.path.join(norm_dir, fname)
                    with open(fpath, "r", encoding="utf-8") as f:
                        data = json.load(f)
                        if isinstance(data, dict):
                            tools.update(data)
        except Exception:
            continue

    return tools

TOOLS = load_tools()

# ====== Clipboard Utility ======
def copy_to_clipboard(text):
    """
    Copy text to system clipboard with zero mandatory dependencies.
    Optionally utilizes pyperclip if installed; falls back gracefully
    to platform-native utilities (clip.exe, pbcopy, xclip, xsel, wl-copy).
    """
    # 1. Try optional pyperclip
    try:
        import pyperclip
        pyperclip.copy(text)
        return True
    except ImportError:
        pass
    except Exception:
        pass

    # 2. Native OS utilities
    if sys.platform == "win32":
        try:
            subprocess.run(["clip"], input=text.encode("utf-8"), shell=True, check=True)
            return True
        except Exception:
            pass
    elif sys.platform == "darwin":
        try:
            subprocess.run(["pbcopy"], input=text.encode("utf-8"), check=True)
            return True
        except Exception:
            pass
    else:
        linux_cmds = [
            ["xclip", "-selection", "clipboard"],
            ["xsel", "--clipboard", "--input"],
            ["wl-copy"]
        ]
        for cmd in linux_cmds:
            try:
                subprocess.run(cmd, input=text.encode("utf-8"), check=True)
                return True
            except Exception:
                continue

    return False

# ====== Variable Substitution ======
def substitute_vars(cmd, target=None, port=None, url=None, lhost=None):
    """Substitute placeholders in commands with user-configured targets."""
    res = cmd
    if target:
        res = res.replace("<IP>", target).replace("<VICTIM_IP>", target)
        if "<URL>" in res and not url:
            prefix = target if target.startswith("http") else f"http://{target}"
            res = res.replace("<URL>", prefix)
    if port:
        res = res.replace("<PORT>", str(port)).replace("<LPORT>", str(port))
    if url:
        res = res.replace("<URL>", url)
    if lhost:
        res = res.replace("<LHOST>", lhost).replace("<ATTACKER_IP>", lhost)
    return res

# ====== Banner UI ======
def banner(target=None, port=None, url=None):
    clear_screen()
    print(f"{RED}")
    print("  ███████╗███████╗██╗     ██╗    ██╗ █████╗ ███╗   ██╗██╗███████╗███╗   ███╗")
    print("  ██╔════╝██╔════╝██║     ██║    ██║██╔══██╗████╗  ██║██║██╔════╝████╗ ████║")
    print("  ███████╗█████╗  ██║     ██║ █╗ ██║███████║██╔██╗ ██║██║███████╗██╔████╔██║")
    print("  ╚════██║██╔══╝  ██║     ██║███╗██║██╔══██║██║╚██╗██║██║╚════██║██║╚██╔╝██║")
    print("  ███████║███████╗███████╗╚███╔███╔╝██║  ██║██║ ╚████║██║███████║██║ ╚═╝ ██║")
    print("  ╚══════╝╚══════╝╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝╚═╝  ╚═══╝╚═╝╚══════╝╚═╝     ╚═╝")
    print(f"{RESET}")
    print(f"  {CYAN}{BOLD}Selwanism v2.1.0{RESET} {GRAY}—{RESET} {WHITE}Personal Pentesting Assistant{RESET}")
    print(f"  {GRAY}{len(TOOLS)} Tools Available {RESET}| {GRAY}Zero Mandatory Dependencies {RESET}| {GRAY}CLI & Interactive REPL{RESET}")
    
    status_parts = []
    if target:
        status_parts.append(f"Target: {GREEN}{target}{RESET}")
    if port:
        status_parts.append(f"Port: {GREEN}{port}{RESET}")
    if url:
        status_parts.append(f"URL: {GREEN}{url}{RESET}")
        
    if status_parts:
        print(f"  {GREEN}[+] Active Bindings:{RESET} {GRAY}|{RESET} ".join(status_parts))
    else:
        print(f"  {YELLOW}[*] Active Targets:{RESET} {GRAY}None (use 'target <IP>' or '-t <IP>' to bind){RESET}")
    print(f"  {GRAY}────────────────────────────────────────────────────────────────────────{RESET}\n")

# ====== Tool View UI ======
def show_tool(name, target=None, port=None, url=None, lhost=None, copy_index=None):
    if name not in TOOLS:
        return False
    tool = TOOLS[name]
    category = tool.get("category", "General")
    
    print(f"\n  {CYAN}┌──────────────────────────────────────────────────────────────────────┐{RESET}")
    header_title = f"{tool['title']}"
    print(f"  {CYAN}│{RESET} {BOLD}{WHITE}{header_title:<68}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {GRAY}Category: {category:<58}{CYAN}│{RESET}")
    print(f"  {CYAN}│{RESET} {WHITE}{tool['desc']:<68}{CYAN}│{RESET}")
    
    bindings = []
    if target:
        bindings.append(f"target={target}")
    if port:
        bindings.append(f"port={port}")
    if url:
        bindings.append(f"url={url}")
    if lhost:
        bindings.append(f"lhost={lhost}")
        
    if bindings:
        bound_str = f"Bound: {', '.join(bindings)}"
        print(f"  {CYAN}│{RESET} {GREEN}{bound_str:<68}{CYAN}│{RESET}")
    print(f"  {CYAN}└──────────────────────────────────────────────────────────────────────┘{RESET}\n")

    copied_cmd = None
    for i, (label, cmd) in enumerate(tool["steps"], 1):
        cmd_display = substitute_vars(cmd, target=target, port=port, url=url, lhost=lhost)
        
        is_copied = (copy_index == i)
        prefix_tag = f"{GREEN}[{i:02d} COPIED]{RESET}" if is_copied else f"{YELLOW}[{i:02d}]{RESET}"
        print(f"    {prefix_tag} {BOLD}{WHITE}{label}{RESET}")
        print(f"         {GREEN}${RESET} {CYAN}{cmd_display}{RESET}\n")
        
        if is_copied:
            copied_cmd = cmd_display

    if copy_index is not None:
        if 1 <= copy_index <= len(tool["steps"]):
            if copy_to_clipboard(copied_cmd):
                print(f"  {GREEN}[+] Successfully copied command [{copy_index:02d}] to clipboard!{RESET}\n")
            else:
                print(f"  {YELLOW}[!] Could not access system clipboard. Install 'pyperclip' or 'xclip'.{RESET}\n")
        else:
            print(f"  {RED}[!] Invalid command number: {copy_index}. Tool has {len(tool['steps'])} commands.{RESET}\n")

    return True

# ====== Search & Discovery ======
def find_matching_tools(query):
    """Token-based and fuzzy similarity matching for tool queries."""
    query_lower = query.lower().strip()
    if not query_lower:
        return []

    # 1. Direct exact key match
    if query_lower in TOOLS:
        return [query_lower]

    tokens = query_lower.split()
    matched_scores = {}

    for key, tool in TOOLS.items():
        key_lower = key.lower()
        title_lower = tool.get("title", "").lower()
        desc_lower = tool.get("desc", "").lower()
        cat_lower = tool.get("category", "").lower()

        score = 0
        if query_lower in key_lower:
            score += 100
        elif all(t in key_lower for t in tokens):
            score += 80

        # Token match across fields
        if all(t in key_lower or t in title_lower or t in desc_lower or t in cat_lower for t in tokens):
            score += 50
        elif any(t in key_lower or t in title_lower or t in desc_lower or t in cat_lower for t in tokens):
            score += 20

        # Match in command bodies
        for _, cmd in tool.get("steps", []):
            if query_lower in cmd.lower():
                score += 15
                break

        if score > 0:
            matched_scores[key] = score

    # 2. Fuzzy difflib match for typos
    if not matched_scores:
        close_keys = difflib.get_close_matches(query_lower, list(TOOLS.keys()), n=4, cutoff=0.5)
        for k in close_keys:
            matched_scores[k] = 35

    return sorted(matched_scores.keys(), key=lambda k: (-matched_scores[k], k))

def search_and_show(query, target=None, port=None, url=None, lhost=None, copy_index=None):
    matches = find_matching_tools(query)

    if not matches:
        print(f"  {RED}[!] No matching tools found for '{query}'{RESET}")
        print(f"  {YELLOW}[*] Run 'sel list' or 'sel -l' to inspect all tools.{RESET}\n")
        return

    if len(matches) == 1:
        show_tool(matches[0], target=target, port=port, url=url, lhost=lhost, copy_index=copy_index)
    else:
        print(f"  {GREEN}[+] Found {len(matches)} matching tools for '{query}':{RESET}")
        for m in matches:
            cat = TOOLS[m].get("category", "General")
            print(f"      {CYAN}•{RESET} {BOLD}{m:<20}{RESET} {GRAY}[{cat:<22}]{RESET} {TOOLS[m]['title']}")
        print(f"\n  {YELLOW}[*] Type 'sel <name>' to view specific tool commands.{RESET}\n")

# ====== List View UI ======
def list_tools():
    print(f"\n  {GREEN}{BOLD}=== Selwanism Pentesting Tools Catalog ({len(TOOLS)} Tools) ==={RESET}")
    categories = {}
    for k, v in TOOLS.items():
        cat = v.get("category", "General")
        categories.setdefault(cat, []).append((k, v["title"]))

    for cat, tools in sorted(categories.items()):
        print(f"\n  {CYAN}{BOLD}┌── {cat} ({len(tools)}){RESET}")
        for k, title in sorted(tools):
            print(f"  {CYAN}│{RESET}   {YELLOW}{k:<20}{RESET} {WHITE}{title}{RESET}")
        print(f"  {CYAN}└──{RESET}")
    print()

# ====== Help Menu UI ======
def help_menu():
    print(f"\n  {GREEN}{BOLD}SELWANISM - Command-Line Interface & Help Menu{RESET}")
    print(f"  {GRAY}────────────────────────────────────────────────────────────────────────{RESET}")
    print(f"  {CYAN}Usage:{RESET}")
    print(f"    sel <tool/keyword>           Direct lookup (e.g. sel nmap, sel sql)")
    print(f"    sel -t <IP> <tool>           Direct lookup with target IP substituted")
    print(f"    sel -t <IP> -c <NUM> <tool>  Copy specific command # to clipboard")
    print(f"    sel list, sel -l             Display categorized list of all tools")
    print(f"    sel -h, --help               Display this help menu")
    print(f"    sel                          Launch interactive REPL mode")
    print()
    print(f"  {CYAN}Options:{RESET}")
    print(f"    -t, --target <IP>            Target IP or hostname")
    print(f"    -p, --port <PORT>            Target or local port number")
    print(f"    -u, --url <URL>              Target URL")
    print(f"    -c, --copy <NUM>             Copy command number directly to clipboard")
    print(f"    -l, --list                   List all tools by category")
    print(f"    -h, --help                   Show this help message")
    print(f"    -v, --version                Show version number")
    print()
    print(f"  {CYAN}Interactive REPL Commands:{RESET}")
    print(f"    target <IP>                  Set active target IP")
    print(f"    port <PORT>                  Set active target port")
    print(f"    url <URL>                    Set active target URL")
    print(f"    set <var> <val>              Set target, port, or url variable")
    print(f"    unset <var/all>              Clear target variables")
    print(f"    vars                         Display current active variables")
    print(f"    copy <tool> <NUM>            Copy specific command to clipboard")
    print(f"    list                         Display categorized list of tools")
    print(f"    clear, cls                   Clear the terminal screen")
    print(f"    exit, quit                   Exit Selwanism")
    print()
    print(f"  {CYAN}Examples:{RESET}")
    print(f"    sel nmap -t 10.10.10.50          View Nmap scan commands for target")
    print(f"    sel nmap -t 10.10.10.50 -c 2     Copy full TCP scan command to clipboard")
    print(f"    sel privesc                      Search Linux & Windows privesc")
    print(f"    sel ad                           Search Active Directory tools")
    print()

# ====== Interactive REPL Mode ======
def interactive_mode(initial_target=None, initial_port=None, initial_url=None):
    vars_state = {
        "target": initial_target,
        "port": initial_port,
        "url": initial_url,
        "lhost": None
    }
    last_tool = None
    
    banner(target=vars_state["target"], port=vars_state["port"], url=vars_state["url"])
    
    while True:
        try:
            prompt_str = f"  {RED}sel{RESET}"
            bound_tags = []
            if vars_state["target"]:
                bound_tags.append(vars_state["target"])
            if vars_state["port"]:
                bound_tags.append(f"p:{vars_state['port']}")
            if bound_tags:
                prompt_str += f"{GRAY}[{GREEN}{':'.join(bound_tags)}{GRAY}]{RESET}"
            prompt_str += f" > "
            user_input = input(prompt_str).strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n  {CYAN}[*] Goodbye.{RESET}")
            break

        if not user_input:
            continue

        parts = user_input.split()
        cmd = parts[0].lower()

        if cmd in ['exit', 'quit']:
            print(f"  {CYAN}[*] Goodbye.{RESET}")
            break
        elif cmd in ['clear', 'cls']:
            banner(target=vars_state["target"], port=vars_state["port"], url=vars_state["url"])
        elif cmd in ['-h', '--help', 'help']:
            help_menu()
        elif cmd in ['vars', 'status']:
            print(f"\n  {GREEN}{BOLD}Current Active Variables:{RESET}")
            print(f"    Target IP: {CYAN}{vars_state['target'] or 'None'}{RESET}")
            print(f"    Port:      {CYAN}{vars_state['port'] or 'None'}{RESET}")
            print(f"    URL:       {CYAN}{vars_state['url'] or 'None'}{RESET}")
            print(f"    LHOST:     {CYAN}{vars_state['lhost'] or 'None'}{RESET}\n")
        elif cmd == 'target':
            if len(parts) > 1:
                vars_state["target"] = parts[1].strip()
                print(f"  {GREEN}[+] Target set to:{RESET} {BOLD}{vars_state['target']}{RESET}\n")
            else:
                print(f"  {YELLOW}[*] Active target:{RESET} {vars_state['target'] or 'None'}\n")
        elif cmd == 'port':
            if len(parts) > 1:
                vars_state["port"] = parts[1].strip()
                print(f"  {GREEN}[+] Port set to:{RESET} {BOLD}{vars_state['port']}{RESET}\n")
            else:
                print(f"  {YELLOW}[*] Active port:{RESET} {vars_state['port'] or 'None'}\n")
        elif cmd == 'url':
            if len(parts) > 1:
                vars_state["url"] = parts[1].strip()
                print(f"  {GREEN}[+] URL set to:{RESET} {BOLD}{vars_state['url']}{RESET}\n")
            else:
                print(f"  {YELLOW}[*] Active URL:{RESET} {vars_state['url'] or 'None'}\n")
        elif cmd == 'set':
            if len(parts) >= 3:
                var_name = parts[1].lower()
                val = parts[2].strip()
                if var_name in vars_state:
                    vars_state[var_name] = val
                    print(f"  {GREEN}[+] {var_name} set to:{RESET} {BOLD}{val}{RESET}\n")
                else:
                    print(f"  {YELLOW}[!] Unknown variable. Valid: target, port, url, lhost{RESET}\n")
            else:
                print(f"  {YELLOW}[*] Usage: set <target|port|url|lhost> <value>{RESET}\n")
        elif cmd == 'unset':
            if len(parts) >= 2:
                var_name = parts[1].lower()
                if var_name in vars_state:
                    vars_state[var_name] = None
                    print(f"  {YELLOW}[*] {var_name} cleared.{RESET}\n")
                elif var_name in ['all', '*']:
                    for k in vars_state:
                        vars_state[k] = None
                    print(f"  {YELLOW}[*] All variables cleared.{RESET}\n")
            else:
                print(f"  {YELLOW}[*] Usage: unset <target|port|url|all>{RESET}\n")
        elif cmd in ['copy', 'cp'] and len(parts) >= 2:
            # Usage: copy <number> (for last_tool) OR copy <tool> <number>
            tool_target = last_tool
            num_str = parts[1]
            if len(parts) >= 3:
                tool_target = parts[1]
                num_str = parts[2]
            
            if not tool_target:
                print(f"  {YELLOW}[!] No tool specified. Usage: copy <tool> <step_number>{RESET}\n")
                continue
            try:
                num = int(num_str)
                show_tool(tool_target, target=vars_state["target"], port=vars_state["port"],
                          url=vars_state["url"], lhost=vars_state["lhost"], copy_index=num)
            except ValueError:
                print(f"  {RED}[!] Invalid command number: {num_str}{RESET}\n")
        elif cmd in ['list', 'all', '-l']:
            list_tools()
        elif user_input.lower().startswith('sel '):
            query = user_input[4:].strip()
            if query.lower() in ['list', 'all', '-l']:
                list_tools()
            else:
                matches = find_matching_tools(query)
                if len(matches) == 1:
                    last_tool = matches[0]
                search_and_show(query, target=vars_state["target"], port=vars_state["port"],
                                url=vars_state["url"], lhost=vars_state["lhost"])
        else:
            matches = find_matching_tools(user_input)
            if len(matches) == 1:
                last_tool = matches[0]
            search_and_show(user_input, target=vars_state["target"], port=vars_state["port"],
                            url=vars_state["url"], lhost=vars_state["lhost"])

# ====== Main Entrypoint ======
def main():
    enable_vt_mode()
    
    parser = argparse.ArgumentParser(
        prog="sel",
        description="SELWANISM — Personal Pentesting Assistant",
        add_help=False
    )
    parser.add_argument("query", nargs="*", help="Tool name or search keyword (e.g. nmap, sql, privesc)")
    parser.add_argument("-t", "--target", type=str, default=None, help="Target IP or hostname to substitute")
    parser.add_argument("-p", "--port", type=str, default=None, help="Target or local port number")
    parser.add_argument("-u", "--url", type=str, default=None, help="Target URL to substitute")
    parser.add_argument("--lhost", type=str, default=None, help="Local listening host IP for reverse shells")
    parser.add_argument("-c", "--copy", type=int, default=None, help="Copy command number to clipboard")
    parser.add_argument("-l", "--list", action="store_true", help="List all available tools")
    parser.add_argument("-h", "--help", action="store_true", help="Show help menu")
    parser.add_argument("-v", "--version", action="version", version="Selwanism 2.1.0")

    args, unknown = parser.parse_known_args()

    if args.help:
        help_menu()
        return

    if args.list:
        list_tools()
        return

    if args.query:
        query_str = " ".join(args.query).strip()
        if query_str.lower() in ["list", "all"]:
            list_tools()
        elif query_str.lower() in ["-h", "--help", "help"]:
            help_menu()
        else:
            search_and_show(query_str, target=args.target, port=args.port,
                            url=args.url, lhost=args.lhost, copy_index=args.copy)
        return

    # No arguments provided: launch interactive mode
    interactive_mode(initial_target=args.target, initial_port=args.port, initial_url=args.url)

if __name__ == "__main__":
    main()
