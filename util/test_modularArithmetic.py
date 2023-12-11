import unittest
from modularArithmetic import multiplicative_inverse, fast_exponent, extended_gcd, gcd, isOdd


class TestModularArithmetic(unittest.TestCase):

    def test_isOdd(self):
        self.assertTrue(isOdd(5))
        self.assertFalse(isOdd(4))

    def test_gcd(self):
        self.assertEqual(gcd(48, 18), 6)
        self.assertEqual(gcd(18, 48), 6)

    def test_multiplicative_inverse(self):
        # Testing known inverses
        self.assertEqual(multiplicative_inverse(3, 11), 4)
        self.assertEqual(multiplicative_inverse(10, 17), 12)

    def test_fast_exponent(self):
        # Testing fast exponentiation
        self.assertEqual(fast_exponent(2, 3, 5), 3)  # 2^3 % 5
        self.assertEqual(fast_exponent(5, 3, 13), 8)  # 5^3 % 13

    def test_extended_gcd(self):
        # Testing extended Euclidean algorithm
        gcd, x, y = extended_gcd(30, 50)
        self.assertEqual(gcd, 10)
        self.assertEqual(30 * x + 50 * y, gcd)

        gcd, x, y = extended_gcd(100, 40)
        self.assertEqual(gcd, 20)
        self.assertEqual(100 * x + 40 * y, gcd)


if __name__ == '__main__':
    unittest.main()
