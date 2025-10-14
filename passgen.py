#!/usr/bin/env python3
"""py-passgen: a tiny CLI password generator."""

import secrets
import string


def generate_password(length: int = 16) -> str:
    """Generate a random password of the given length."""
    alphabet = string.ascii_letters + string.digits
    return "".join(secrets.choice(alphabet) for _ in range(length))


def main() -> None:
    print(generate_password())


if __name__ == "__main__":
    main()
