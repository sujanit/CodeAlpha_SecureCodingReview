
import ast
import re
import sys
from pathlib import Path

RULES = [
    (
        "SC001",
        "Possible hardcoded password or secret",
        re.compile(
            r"""(?i)\b(password|passwd|secret|api_key)\s*=\s*['"][^'"]+['"]"""
        ),
    ),
    ("SC002", "Use of eval()", re.compile(r"\beval\s*\(")),
    ("SC003", "Use of exec()", re.compile(r"\bexec\s*\(")),
    (
        "SC004",
        "Possible SQL query built with string formatting",
        re.compile(
            r"""(?i)\b(SELECT|INSERT|UPDATE|DELETE)\b.*(%s|\.format\s*\(|f['"])"""
        ),
    ),
]


def scan_file(filename):
    path = Path(filename)

    if not path.is_file() or path.suffix.lower() != ".py":
        print(f"Skipping: {filename} (not a Python file)")
        return

    try:
        source = path.read_text(encoding="utf-8")
    except (OSError, UnicodeError) as error:
        print(f"Could not read {filename}: {error}")
        return

    print(f"\nScanning: {path}")

    try:
        ast.parse(source, filename=str(path))
    except SyntaxError as error:
        print(
            f"[INFO] Python syntax issue at line "
            f"{error.lineno}: {error.msg}"
        )

    findings = 0

    for number, line in enumerate(source.splitlines(), start=1):
        for rule_id, description, pattern in RULES:
            if pattern.search(line):
                print(f"[{rule_id}] Line {number}: {description}")
                findings += 1

    if findings == 0:
        print("No matching patterns found.")

    print(f"Review complete: {findings} potential finding(s).")
    print("Findings require manual verification.")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python scanner.py <python_file>")
        sys.exit(1)

    scan_file(sys.argv[1])
