import unittest
from closest_triplet_sum import closest_triplet_sum

class TestClosestTripletSum(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(closest_triplet_sum([1, 2, 3, 4, 5], 10), 10)

    def test_example2(self):
        self.assertEqual(closest_triplet_sum([-1, 2, 1, -4], 1), 2)

    def test_example3(self):
        self.assertEqual(closest_triplet_sum([0, 0, 0], 1), 0)

    def test_multiple_closest(self):
        self.assertEqual(closest_triplet_sum([1, 1, 1, 0], 100), 3)

    def test_large_input(self):
        self.assertEqual(closest_triplet_sum(list(range(-1000, 1000)), 3), 3)

if __name__ == '__main__':
    unittest.main()
