import unittest
from square_sort import square_sort

class TestSquareSort(unittest.TestCase):
    def test_positive_and_negative(self):
        self.assertEqual(square_sort([-4, -1, 0, 3, 10]), [0, 1, 9, 16, 100])
    def test_all_negative(self):
        self.assertEqual(square_sort([-7, -3, -1]), [1, 9, 49])
    def test_all_positive(self):
        self.assertEqual(square_sort([1, 2, 3]), [1, 4, 9])
    def test_single_element(self):
        self.assertEqual(square_sort([5]), [25])

if __name__ == "__main__":
    unittest.main()
