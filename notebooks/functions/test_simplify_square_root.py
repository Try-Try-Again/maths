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
         
    def test_sqrt_of_18_returns_3_and_2(self):
        whole_num, sqrt_num = simplify_square_root(1, 18)
        self.assertEqual(whole_num, 3)
        self.assertEqual(sqrt_num, 2)
    
    def test_sqrt_of_108_returns_6_and_3(self):
        whole_num, sqrt_num = simplify_square_root(1, 108)
        self.assertEqual(whole_num, 6)
        self.assertEqual(sqrt_num, 3)
        
    def test_sqrt_of_28_returns_2_and_7(self):
        whole_num, sqrt_num = simplify_square_root(1, 28)
        self.assertEqual(whole_num, 2)
        self.assertEqual(sqrt_num, 7)
        
    def test_sqrt_of_450_returns_15_2(self):
        whole_num, sqrt_num = simplify_square_root(15, 2)
        self.assertEqual(whole_num, 15)
        self.assertEqual(sqrt_num, 2)


    
if __name__ == '__main__':
    unittest.main()

   