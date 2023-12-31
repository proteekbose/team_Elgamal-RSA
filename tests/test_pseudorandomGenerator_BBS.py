import unittest
from unittest.mock import patch
from util.pseudorandomGenerator_BBS import find_seed, generate_bit, generate_random_number, rand_gen
from util.modularArithmetic import gcd

class TestPseudorandomGeneratorBBS(unittest.TestCase):

    def test_find_seed(self):
        # Assuming p and q are 3-digit primes and p*q is the modulus
        p = 101  # 3-digit prime
        q = 103  # 3-digit prime
        modulus = p * q
        seed = find_seed(modulus)

        # The seed should be relatively prime to the modulus
        self.assertEqual(gcd(seed, modulus), 1)

    def test_generate_bit(self):
        p = 101  # 3-digit prime
        q = 103  # 3-digit prime
        modulus = p * q

        # Test if generate_bit returns a bit (0 or 1)
        bit = generate_bit(modulus)
        self.assertIn(bit, [0, 1])

    @patch('util.pseudorandomGenerator_BBS.generate_bit')
    def test_generate_random_number(self, mock_generate_bit):
        # Mock generate_bit to return a predictable sequence
        mock_generate_bit.side_effect = [1, 0, 1, 1]  # Example 4-bit sequence

        p = 101  # 3-digit prime
        q = 103  # 3-digit prime
        bit_count = 4
        random_number = generate_random_number(bit_count, p, q)

        # Convert the sequence [1, 0, 1, 1] to an integer
        expected_number = int('1011', 2)
        self.assertEqual(random_number, expected_number)

    @patch('util.pseudorandomGenerator_BBS.generate_random_number')
    def test_rand_gen(self, mock_generate_random_number):
        # Mock generate_random_number to return a fixed value
        expected_number = 123
        mock_generate_random_number.return_value = expected_number

        # Test if rand_gen returns the mocked value
        self.assertEqual(rand_gen(), expected_number)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
