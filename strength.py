#!/usr/bin/env python3
"""Estimate password strength from character variety and length."""

import math
import string


def entropy_bits(password: str) -> float:
    """Rough entropy estimate in bits."""
    pool = 0
    if any(c in string.ascii_lowercase for c in password):
        pool += 26
    if any(c in string.ascii_uppercase for c in password):
        pool += 26
    if any(c in string.digits for c in password):
        pool += 10
    if any(c in string.punctuation for c in password):
        pool += len(string.punctuation)
    if pool == 0:
        return 0.0
    return len(password) * math.log2(pool)


def strength_label(password: str) -> str:
    bits = entropy_bits(password)
    if bits < 40:
        return "weak"
    if bits < 60:
        return "fair"
    if bits < 80:
        return "strong"
    return "excellent"
