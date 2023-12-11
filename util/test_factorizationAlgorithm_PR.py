import unittest
from unittest.mock import patch
from factorizationAlgorithm_PR import (
    pollards_rho_factor,
    find_factors,
    smallest_prime_factor,
    all_prime_factors,
    primitive_root_search,
    is_primitive_root
)


class TestFactorizationAlgorithmPR(unittest.TestCase):

    def test_pollards_rho_factor(self):
        # Testing with a known composite number
        self.assertEqual(pollards_rho_factor(15), 3)

    def test_find_factors(self):
        # Testing with a known composite number
        factors = find_factors(21)
        self.assertIn(3, factors)
        self.assertIn(7, factors)

    def test_smallest_prime_factor(self):
        # Testing with a number that has a small prime factor
        self.assertEqual(smallest_prime_factor(77), 7)

    def test_all_prime_factors(self):
        # Testing with a composite number
        expected_factors = sorted([2, 3, 5])
        actual_factors = sorted(all_prime_factors(30))
        self.assertListEqual(actual_factors, expected_factors)


    def test_primitive_root_search(self):
        p = 11  # Use a prime number
        found_root = primitive_root_search(p)
        # Check if the found root is indeed a primitive root
        self.assertTrue(is_primitive_root(found_root, p))

    def test_is_primitive_root(self):
        # Example: Testing with a known primitive root (if available)
        # Replace 2 and 11 with a known primitive root and its corresponding number
        self.assertTrue(is_primitive_root(2, 11))

        # Generic approach: Find a primitive root using the function and then check
        p = 11  # Use a prime number
        primitive_root = primitive_root_search(p)
        self.assertTrue(is_primitive_root(primitive_root, p))


if __name__ == '__main__':
    unittest.main()
