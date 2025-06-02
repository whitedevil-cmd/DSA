import unittest
from main import evaluate_postfix

class TestEvaluatePostfix(unittest.TestCase):
    def test_valid(self):
        self.assertEqual(evaluate_postfix(["2", "3", "+"]), 5)
        self.assertEqual(evaluate_postfix(["4", "13", "5", "/", "+"]), 6)
        self.assertEqual(evaluate_postfix(["10", "6", "9", "3", "/", "-", "*"]), 30)

    def test_errors(self):
        self.assertIn("Division by zero", evaluate_postfix(["10", "0", "/"]))
        self.assertIn("Not enough operands", evaluate_postfix(["+"]))
        self.assertIn("Invalid token", evaluate_postfix(["2", "a", "+"]))
        self.assertIn("Malformed", evaluate_postfix(["2", "3"]))

if __name__ == "__main__":
    unittest.main()
