#!/usr/bin/env python3
"""py-passgen: a tiny CLI password generator."""

import argparse
import secrets
import string

from strength import entropy_bits, strength_label


def build_alphabet(use_symbols: bool = True, use_digits: bool = True) -> str:
    alphabet = string.ascii_letters
    if use_digits:
        alphabet += string.digits
    if use_symbols:
        alphabet += "!@#$%^&*()-_=+[]{}"
    return alphabet


def generate_password(length: int = 16, use_symbols: bool = True,
                      use_digits: bool = True) -> str:
    """Generate a random password of the given length."""
    alphabet = build_alphabet(use_symbols, use_digits)
    return "".join(secrets.choice(alphabet) for _ in range(length))


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate secure passwords.")
    parser.add_argument("-l", "--length", type=int, default=16,
                        help="password length (default: 16)")
    parser.add_argument("-n", "--count", type=int, default=1,
                        help="how many passwords to generate")
    parser.add_argument("--no-symbols", action="store_true",
                        help="exclude punctuation characters")
    parser.add_argument("--no-digits", action="store_true",
                        help="exclude digits")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    for _ in range(args.count):
        pwd = generate_password(args.length, not args.no_symbols,
                                not args.no_digits)
        print(f"{pwd}  [{strength_label(pwd)}, {entropy_bits(pwd):.0f} bits]")


if __name__ == "__main__":
    main()
