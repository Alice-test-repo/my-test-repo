"""Tests for the repository's hello-world script."""

import subprocess
import sys
import unittest
from pathlib import Path


SCRIPT_PATH = Path(__file__).with_name("test.py")


class HelloScriptTests(unittest.TestCase):
    def test_script_prints_hello(self) -> None:
        result = subprocess.run(
            [sys.executable, str(SCRIPT_PATH)],
            capture_output=True,
            check=True,
            text=True,
        )

        self.assertEqual(result.stdout, "hello\n")
        self.assertEqual(result.stderr, "")


if __name__ == "__main__":
    unittest.main()
