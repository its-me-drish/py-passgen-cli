# py-passgen-cli

A tiny command-line password generator written in Python. Zero dependencies,
standard library only.

## Usage

```bash
python passgen.py                  # one 16-char password
python passgen.py -l 24 -n 5       # five 24-char passwords
python passgen.py --no-symbols     # letters and digits only
```

Each password is printed with its strength label and estimated entropy.

## Options

| Flag | Description |
| --- | --- |
| `-l`, `--length` | Password length (default 16) |
| `-n`, `--count` | Number of passwords to generate |
| `--no-symbols` | Exclude punctuation |
| `--no-digits` | Exclude digits |

## Strength checking

`strength.py` estimates password entropy (in bits) and labels a
password as weak, fair, strong, or excellent.

## Running the tests

```bash
python -m unittest test_passgen.py
```

## License

MIT
