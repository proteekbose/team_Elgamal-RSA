import unittest
from unittest.mock import patch, MagicMock
from primalityTest_MR import get_modulus, is_prime, get_primes


class TestPrimalityTestMR(unittest.TestCase):

    # Test cases for get_modulus
    @patch('primalityTest_MR.get_primes')
    def test_get_modulus_with_valid_output(self, mock_get_primes):
        mock_get_primes.return_value = [7, 11]
        expected_modulus = 7 * 11
        expected_prime1 = 7
        expected_prime2 = 11
        actual_modulus, actual_prime1, actual_prime2 = get_modulus(2, 1)
        self.assertEqual(actual_modulus, expected_modulus)
        self.assertEqual(actual_prime1, expected_prime1)
        self.assertEqual(actual_prime2, expected_prime2)

    @patch('primalityTest_MR.get_primes')
    def test_get_modulus_returns_three_values(self, mock_get_primes):
        mock_get_primes.return_value = [13, 17]
        result = get_modulus(2, 2)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(x, int) for x in result))

    # Test cases for is_prime
    def test_is_prime_with_prime_number(self):
        self.assertTrue(is_prime(13))

    def test_is_prime_with_non_prime_number(self):
        self.assertFalse(is_prime(15))


if __name__ == '__main__':
    unittest.main()
