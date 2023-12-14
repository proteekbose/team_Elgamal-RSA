import unittest
from util.keyGenerator_BSGS import baby_giant_step


class TestBabyGiantStep(unittest.TestCase):

    def test_baby_giant_step(self):
        # Example test case: solve b^l ≡ a (mod n) for known values
        a = 5  # a value for the congruence equation
        b = 2  # base value for the congruence equation
        n = 11  # modulus value for the congruence equation
        expected_l = 4  # Expected solution for the logarithm problem (since 2^4 % 11 == 5)

        # Test
        actual_l = baby_giant_step(a, b, n)
        self.assertEqual(actual_l, expected_l)


if __name__ == '__main__':  # pragma: no cover
    unittest.main()
