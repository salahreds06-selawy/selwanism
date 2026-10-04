import subprocess
import sys
import os
import unittest

SEL_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "sel")

class TestSelwanismCLI(unittest.TestCase):
    def run_sel(self, *args):
        cmd = [sys.executable, SEL_PATH] + list(args)
        proc = subprocess.run(
            cmd,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            encoding="utf-8",
            errors="replace"
        )
        return proc

    def test_direct_tool_lookup(self):
        res = self.run_sel("nmap")
        self.assertEqual(res.returncode, 0)
        self.assertIn("Nmap - Network Scanner", res.stdout)
        self.assertIn("Quick scan", res.stdout)
        self.assertIn("nmap -sV", res.stdout)

    def test_target_substitution(self):
        res = self.run_sel("-t", "192.168.1.150", "-p", "8443", "nmap")
        self.assertEqual(res.returncode, 0)
        self.assertIn("target=192.168.1.150", res.stdout)
        self.assertIn("nmap -sV 192.168.1.150", res.stdout)
        self.assertNotIn("<IP>", res.stdout)

    def test_list_tools(self):
        res = self.run_sel("list")
        self.assertEqual(res.returncode, 0)
        self.assertIn("Reconnaissance", res.stdout)
        self.assertIn("Active Directory", res.stdout)
        self.assertIn("Web Application", res.stdout)
        self.assertIn("Pivoting & Tunneling", res.stdout)
        self.assertIn("nmap", res.stdout)
        self.assertIn("chisel", res.stdout)

    def test_help_flag(self):
        res = self.run_sel("-h")
        self.assertEqual(res.returncode, 0)
        self.assertIn("SELWANISM - Command-Line Interface", res.stdout)
        self.assertIn("Usage:", res.stdout)

    def test_search_partial_query(self):
        res = self.run_sel("privesc")
        self.assertEqual(res.returncode, 0)
        self.assertIn("linux_privesc", res.stdout)
        self.assertIn("windows_privesc", res.stdout)

    def test_fuzzy_search(self):
        res = self.run_sel("nmapp")
        self.assertEqual(res.returncode, 0)
        self.assertIn("Nmap - Network Scanner", res.stdout)

    def test_clipboard_copy_flag(self):
        res = self.run_sel("-t", "10.10.10.10", "nmap", "-c", "1")
        self.assertEqual(res.returncode, 0)
        self.assertIn("[01 COPIED]", res.stdout)

    def test_modern_active_directory_tools(self):
        for tool in ["kerberoast", "asrep_roasting", "adcs", "secretsdump"]:
            res = self.run_sel(tool)
            self.assertEqual(res.returncode, 0)
            self.assertIn("Active Directory", res.stdout)

    def test_modern_web_tools(self):
        for tool in ["ffuf", "ssrf", "jwt_attacks", "websocket_hijacking"]:
            res = self.run_sel(tool)
            self.assertEqual(res.returncode, 0)
            self.assertIn("Web Application", res.stdout)

    def test_pivoting_tools(self):
        for tool in ["chisel", "ligolo_ng", "ssh_tunneling"]:
            res = self.run_sel(tool)
            self.assertEqual(res.returncode, 0)
            self.assertIn("Pivoting & Tunneling", res.stdout)

    def test_database_integrity(self):
        # Execute sel in a fresh namespace to import TOOLS without running main()
        namespace = {"__name__": "__not_main__", "__file__": SEL_PATH}
        with open(SEL_PATH, encoding="utf-8") as f:
            source = f.read()
        exec(compile(source, SEL_PATH, "exec"), namespace)
        tools = namespace["TOOLS"]
        self.assertGreaterEqual(len(tools), 36)
        for name, data in tools.items():
            self.assertIn("title", data, f"Tool {name} missing title")
            self.assertIn("category", data, f"Tool {name} missing category")
            self.assertIn("desc", data, f"Tool {name} missing desc")
            self.assertIn("steps", data, f"Tool {name} missing steps")
            self.assertGreater(len(data["steps"]), 0, f"Tool {name} has no steps")

if __name__ == "__main__":
    unittest.main()
