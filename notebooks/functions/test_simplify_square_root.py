import unittest
from simplify_square_root import simplify_square_root


class SimplifyingSquareRoot(unittest.TestCase):

    def test_sqrt_of_75_returns_5_and_3(self):
        whole_num, sqrt_num = simplify_square_root(1, 75)
        self.assertEqual(whole_num, 5)
        self.assertEqual(sqrt_num, 3)

    def test_5_times_sqrt_of_117_returns_15_and_13(self):
        whole_num, sqrt_num = simplify_square_root(5, 117)
        self.assertEqual(whole_num, 15)
        self.assertEqual(sqrt_num, 13)
        
if __name__ == '__main__':
    unittest.main()
