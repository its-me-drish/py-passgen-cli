# py-passgen-cli

A tiny command-line password generator written in Python.

## Usage

```bash
python passgen.py
```

Prints one random 16-character password to stdout.

## Strength checking

`strength.py` estimates password entropy (in bits) and labels a
password as weak, fair, strong, or excellent.
