# Selwanism Codebase Inspection Report

## Executive Summary
This report analyzes the architecture, execution behavior, and code quality of `selwanism` (version 2.0).
The tool provides ready-to-use cheatsheets for 23 penetration testing tools.

## Architecture Analysis
- Main Entrypoint: `sel` (single-file executable Python script, 392 lines).
- Data Storage: `TOOLS` dictionary hardcoded directly in `sel`.
- User Interface: ANSI terminal colors with raw `print` loops and `input()` prompt.
- Shell Installation: `install.sh` bash script.

## Core Findings and Defects

### 1. Command-Line Arguments Ignored
- Location: `sel#L360-L389` (`main()` function)
- Defect: `main()` does not inspect `sys.argv`.
- Impact: Documented CLI commands such as `sel nmap`, `sel list`, and `sel -h` in `README.md` fail to execute directly. Running them unconditionally launches the interactive prompt.

### 2. Windows Incompatibility in Screen Clear
- Location: `sel#L280-L281` (`banner()` function)
- Defect: Invokes `os.system('clear')` directly.
- Impact: On Windows systems, `clear` is not recognized, printing shell error messages and failing to clear the screen cleanly.

### 3. Destructive Installation Script
- Location: `install.sh#L12`
- Defect: Uses `sudo mv sel /usr/local/bin/sel` instead of `cp`.
- Impact: Running `install.sh` removes `sel` from the local cloned repository.

### 4. Monolithic and Coupled Cheatsheet Storage
- Location: `sel#L20-L277` (`TOOLS` dictionary)
- Defect: Cheatsheet content is embedded directly into Python source code.
- Impact: Adding or modifying cheatsheets requires editing executable code, increasing regression risk and complicating open-source contributions.

### 5. Search Engine Limitations
- Location: `sel#L307-L329` (`search_and_show()` function)
- Defect: Search relies on basic substring matching against key, title, and description.
- Impact: No support for categories, tags, command syntax searching, or typo tolerance.

### 6. Static Placeholders Without Variable Substitution
- Location: `sel#L25-L275`
- Defect: Commands contain static tokens like `<IP>`, `<PORT>`, and `<URL>`.
- Impact: Users must manually re-type or edit every command after copying.
