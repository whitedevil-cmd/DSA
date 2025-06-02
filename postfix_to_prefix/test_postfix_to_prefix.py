import unittest
from postfix_to_prefix import postfix_to_prefix

class TestPostfixToPrefix(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(postfix_to_prefix("AB+"), "+AB")
        self.assertEqual(postfix_to_prefix("ABC*+"), "+A*BC")
        self.assertEqual(postfix_to_prefix("AB+C*"), "*+ABC")
        self.assertEqual(postfix_to_prefix("ABCD^/-"), "-/AB^CD")

if __name__ == "__main__":
    unittest.main()
