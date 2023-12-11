# Blum-Blum-Shub Pseudorandom Number Generator
import random
from util import modularArithmetic as ma


def find_seed(modulus):
    # Finds a seed that is relatively prime to the given modulus.
    seed = random.randint(1, modulus)
    while ma.gcd(seed, modulus) != 1:
        seed = random.randint(1, modulus)
    return seed


def generate_bit(modulus):
    # Generates a single bit using the Blum-Blum-Shub method.
    seed = find_seed(modulus)
    for _ in range(modulus):
        seed = (seed ** 2) % modulus
    return seed % 2


def generate_random_number(bit_count, p, q):
    # Generates a random number using the Blum-Blum-Shub method.
    modulus = p * q
    return int(''.join(str(generate_bit(modulus)) for _ in range(bit_count)), 2)


def rand_gen():
    # Generates a 24-bit random number using specific prime numbers.
    return generate_random_number(24, 11, 23)

