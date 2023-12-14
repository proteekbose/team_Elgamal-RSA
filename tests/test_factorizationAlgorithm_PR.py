import unittest

from util.factorizationAlgorithm_PR import (
    pollards_rho_factor,
    find_factors,
    smallest_prime_factor,
    all_prime_factors,
    primitive_root_search,
    is_primitive_root
)


class TestFactorizationAlgorithmPR(unittest.TestCase):

    def test_pollards_rho_factor(self):
        test_cases = [
            (15, 3),
            (16420634371030736081, 4043235727),  # large composite number
            (13, -1)  # prime number
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(pollards_rho_factor(n), expected)

    def test_find_factors(self):
        test_cases = [
            (21, [3, 7]),
            (16420634371030736081, [4043235727, 4061260703]),  # large composite number
            (13, [-1, -1])  # prime number
        ]
        for n, expected_factors in test_cases:
            with self.subTest(n=n):
                factors = find_factors(n)
                for factor in expected_factors:
                    self.assertIn(factor, factors)

    def test_smallest_prime_factor(self):
        test_cases = [
            (77, 7),
            (16420634371030736081, 4043235727)  # large number
        ]
        for n, expected in test_cases:
            with self.subTest(n=n):
                self.assertEqual(smallest_prime_factor(n), expected)

    def test_all_prime_factors(self):
        test_cases = [
            (30, [2, 3, 5]),
            (16420634371030736081, [4043235727, 4061260703])  # large number
        ]
        for n, expected_factors in test_cases:
            with self.subTest(n=n):
                actual_factors = sorted(all_prime_factors(n))
                self.assertListEqual(actual_factors, sorted(expected_factors))

    def test_primitive_root_search(self):
        test_primes = [11, 839, 50374586549039]  # large primes
        for p in test_primes:
            with self.subTest(p=p):
                root = primitive_root_search(p)
                self.assertTrue(is_primitive_root(root, p))

    def test_pollards_rho_factor_with_prime(self):
        # Testing with a prime number, which should return -1
        self.assertEqual(pollards_rho_factor(13), -1)

    def test_find_factors_with_prime(self):
        # Testing with a prime number, which should return (-1, -1)
        factors = find_factors(13)
        self.assertEqual(factors, (-1, -1))


if __name__ == '__main__':  # pragma: no cover
    unittest.main()

