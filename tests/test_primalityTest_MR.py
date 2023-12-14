import unittest
from unittest.mock import patch, MagicMock
from util.primalityTest_MR import get_modulus, is_prime, get_primes


class TestPrimalityTestMR(unittest.TestCase):

    # Test cases for get_modulus
    @patch('util.primalityTest_MR.get_primes')
    def test_get_modulus_with_valid_output(self, mock_get_primes):
        mock_get_primes.return_value = [123457, 123459]
        expected_modulus = 123457 * 123459
        expected_prime1 = 123457
        expected_prime2 = 123459
        actual_modulus, actual_prime1, actual_prime2 = get_modulus(2, 1)
        self.assertEqual(actual_modulus, expected_modulus)
        self.assertEqual(actual_prime1, expected_prime1)
        self.assertEqual(actual_prime2, expected_prime2)

    @patch('util.primalityTest_MR.get_primes')
    def test_get_modulus_returns_three_values(self, mock_get_primes):
        mock_get_primes.return_value = [987643, 987653]
        result = get_modulus(2, 2)
        self.assertEqual(len(result), 3)
        self.assertTrue(all(isinstance(x, int) for x in result))

    # Test cases for is_prime
    def test_is_prime_with_large_prime_number(self):
        # Testing with a large prime number
        self.assertTrue(is_prime(104729))  # Known large prime

    def test_get_primes_default_rand(self):
        # Test using the default random number generator
        primes = get_primes(2, 0)
        self.assertEqual(len(primes), 2)
        self.assertTrue(all(is_prime(p) for p in primes))

    def test_get_primes_nr_rand_gen(self):
        # Test using the Naor-Reingold pseudorandom number generator
        primes = get_primes(2, 1)
        self.assertEqual(len(primes), 2)
        self.assertTrue(all(is_prime(p) for p in primes))

    def test_get_primes_bbs_rand_gen(self):
        # Test using the Blum-Blum-Shub pseudorandom number generator with larger primes
        primes = get_primes(2, 2)
        self.assertEqual(len(primes), 2)
        self.assertTrue(all(is_prime(p) and p > 10000 for p in primes))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
