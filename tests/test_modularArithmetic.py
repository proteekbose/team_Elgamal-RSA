import unittest
from util.modularArithmetic import multiplicative_inverse, fast_exponent, extended_gcd, gcd, isOdd

class TestModularArithmetic(unittest.TestCase):

    def test_isOdd(self):
        self.assertTrue(isOdd(100001))
        self.assertFalse(isOdd(100000))

    def test_gcd(self):
        self.assertEqual(gcd(123456, 789012), 12)
        self.assertEqual(gcd(789012, 123456), 12)

    def test_multiplicative_inverse(self):
        # Testing known inverses with larger values
        self.assertEqual(multiplicative_inverse(10, 17), 12)  # Example small value
        self.assertEqual(multiplicative_inverse(3, 11), 4)

    def test_multiplicative_inverse_no_solution(self):
        # Test case where no multiplicative inverse exists
        self.assertEqual(multiplicative_inverse(123456, 789012), -1)  # Not coprime

    def test_fast_exponent(self):
        # Testing fast exponentiation with larger values
        self.assertEqual(fast_exponent(2, 3, 5), 3)  # 2^3 % 5
        self.assertEqual(fast_exponent(5, 3, 13), 8)  # 5^3 % 13

    def test_extended_gcd(self):
        # Testing extended Euclidean algorithm with larger values
        gcd, x, y = extended_gcd(123456, 789012)
        self.assertEqual(gcd, 12)
        self.assertEqual(123456 * x + 789012 * y, gcd)

        gcd, x, y = extended_gcd(100, 40)
        self.assertEqual(gcd, 20)
        self.assertEqual(100 * x + 40 * y, gcd)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
