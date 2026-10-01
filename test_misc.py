"""Miscellaneous smoke tests for the repository."""

import unittest


class MiscTests(unittest.TestCase):
    def test_python_arithmetic(self) -> None:
        """Sanity-check basic arithmetic."""
        self.assertEqual(2 + 2, 4)
        self.assertAlmostEqual(0.1 + 0.2, 0.3, places=10)

    def test_string_helpers(self) -> None:
        """Sanity-check common string operations."""
        phrase = "hello, world"
        self.assertEqual(phrase.upper(), "HELLO, WORLD")
        self.assertEqual(phrase.split(", "), ["hello", "world"])
        self.assertTrue(phrase.startswith("hello"))

    def test_list_operations(self) -> None:
        """Sanity-check common list operations."""
        numbers = [3, 1, 2]
        self.assertEqual(sorted(numbers), [1, 2, 3])
        self.assertEqual(len(numbers), 3)
        self.assertEqual(sum(numbers), 6)
        self.assertIn(2, numbers)


if __name__ == "__main__":
    unittest.main()
