import unittest
from cure_all_patients import cure_all_patients

class TestCureAllPatients(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(cure_all_patients([3, 6, 7], [1, 2, 5]), "Yes")
        self.assertEqual(cure_all_patients([1, 2, 3], [1, 2, 3]), "No")
        self.assertEqual(cure_all_patients([5, 6], [3, 7]), "No")

    def test_unequal_length(self):
        self.assertEqual(cure_all_patients([1, 2], [1]), "No")
        self.assertEqual(cure_all_patients([1], [1, 2]), "No")

if __name__ == "__main__":
    unittest.main()
