import unittest
from unittest.mock import patch
from pseudorandomGenerator_NR import (
    generate_a, find_square, generate_b,
    generate_bit, generate_random_number, rand_gen, rand_gen_bi
)


class TestPseudorandomGeneratorNR(unittest.TestCase):

    def test_generate_a(self):
        # Testing based on known inputs and expected format of the output
        n = 6
        modulus = 47 * 37
        x = 43
        result = generate_a(n, modulus, x)
        self.assertIsInstance(result, int)

    def test_find_square(self):
        modulus = 47
        square = find_square(modulus)
        self.assertTrue(0 < square < modulus)

    def test_generate_b(self):
        n = 6
        binary_string = generate_b(n)
        self.assertEqual(len(binary_string), 2 * n)
        self.assertTrue(all(c in '01' for c in binary_string))

    def test_generate_bit(self):
        n = 6
        p = 47
        q = 37
        x = 43
        bit = generate_bit(n, p, q, x)
        self.assertIn(bit, [0, 1])

    def test_generate_random_number(self):
        bit_count = 24
        random_number = generate_random_number(bit_count)
        self.assertIsInstance(random_number, int)

    def test_rand_gen(self):
        random_number = rand_gen()
        self.assertIsInstance(random_number, int)

    def test_rand_gen_bi(self):
        random_binary_string = rand_gen_bi()
        self.assertEqual(len(random_binary_string), 24)
        self.assertTrue(all(c in '01' for c in random_binary_string))


if __name__ == '__main__':
    unittest.main()
