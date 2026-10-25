
# CodeAlpha Secure Coding Review

## Overview
A beginner-friendly Python source-code scanner developed as a cybersecurity learning project for reviewing common security-risk patterns.

## Features
- Detects possible hardcoded passwords and secrets.
- Flags uses of eval() and exec().
- Identifies possible SQL query string-formatting risks.
- Reports the source file and line number for each finding.
- Checks Python syntax and reports syntax issues.

## Technologies
- Python 3
- Regular expressions
- Python AST module

## Requirements
- Python 3 installed on your system.

## Usage
Run the scanner against a Python file:

```bash
python scanner.py sample_vulnerable.py
```

Replace the sample filename with another Python source file to review.

## Limitations
This is a pattern-based educational scanner. Findings require manual verification. It can produce false positives and miss security vulnerabilities. It is not a replacement for a professional security audit.

## Disclaimer
Use this tool only on source code you own or are authorized to review. The sample vulnerable file is intended for local testing only.
