import unittest
from max_score import max_score

class TestMaxScore(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(max_score([100, 200, 300, 400], 200), 2)

    def test_case_2(self):
        self.assertEqual(max_score([100], 50), 0)

    def test_case_3(self):
        self.assertEqual(max_score([100, 200], 150), 1)

    def test_case_4(self):
        self.assertEqual(max_score([100, 200, 300], 250), 2)

if __name__ == "__main__":
    unittest.main()
