# Naor-Reingold Pseudorandom Number Generator
import random
from util import modularArithmetic as ma


def generate_a(n, modulus, x):
    # Generates 'a' values based on Naor-Reingold algorithm.
    g = find_square(modulus)
    a_values = [random.randint(1, modulus) for _ in range(2 * n)]
    binary_x = [int(d) for d in bin(x)[2:].zfill(n)]

    return ma.fast_exponent(sum(a_values[i] for i in range(n) if binary_x[i]), modulus, g)


def find_square(modulus):
    # Finds a square number that is relatively prime to the given modulus.
    while True:
        sqrt_candidate = random.randint(1, modulus)
        if ma.gcd(sqrt_candidate, modulus) == 1:
            return pow(sqrt_candidate, 2, modulus)


def generate_b(n):
    # Generates random binary string of length 2n.
    return ''.join(str(random.randint(0, 1)) for _ in range(2 * n))


def generate_bit(n, p, q, x):
    # Generates a single bit using Naor-Reingold algorithm.
    num = generate_a(n, p * q, x)
    a_bin = bin(num)[2:].zfill(2 * n)
    b_bin = generate_b(n)

    return int(a_bin[-1]) * int(b_bin[-1])


def generate_random_number(bit_count, n=6, p=47, q=37, x=43):
    # Generates a random number using the Naor-Reingold method.
    return int(''.join(str(generate_bit(n, p, q, x)) for _ in range(bit_count)), 2)


def rand_gen():
    # Generates a 24-bit random number.
    return generate_random_number(24)


def rand_gen_bi():
    # Generate a 24-bit binary string.
    return ''.join(str(generate_bit(6, 47, 37, 43)) for _ in range(24))
