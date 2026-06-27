import unittest

from passgen import build_alphabet, generate_password
from strength import entropy_bits, strength_label


class GeneratePasswordTests(unittest.TestCase):
    def test_default_length(self):
        self.assertEqual(len(generate_password()), 16)

    def test_custom_length(self):
        self.assertEqual(len(generate_password(32)), 32)

    def test_no_digits(self):
        pwd = generate_password(64, use_digits=False)
        self.assertFalse(any(c.isdigit() for c in pwd))

    def test_alphabet_without_symbols(self):
        self.assertNotIn("!", build_alphabet(use_symbols=False))


class StrengthTests(unittest.TestCase):
    def test_empty_password_has_zero_entropy(self):
        self.assertEqual(entropy_bits(""), 0.0)

    def test_short_password_is_weak(self):
        self.assertEqual(strength_label("abc"), "weak")

    def test_long_mixed_password_is_strong(self):
        self.assertIn(strength_label(generate_password(24)),
                      ("strong", "excellent"))


if __name__ == "__main__":
    unittest.main()
