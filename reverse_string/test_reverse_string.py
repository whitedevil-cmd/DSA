import unittest
from reverse_string import reverse

class TestReverseFunction(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(reverse("hello"), "olleh")
        self.assertEqual(reverse("abc"), "cba")
        self.assertEqual(reverse(""), "")
        self.assertEqual(reverse("a"), "a")
        self.assertEqual(reverse("12345"), "54321")

if __name__ == "__main__":
    unittest.main()
