# Pollard’s Rho Factorization Algorithm and Related Functions for Elgamal Cryptosystem
from util import modularArithmetic as ma
from util import primalityTest_MR as ptmr
import random

is_prime = lambda n: ptmr.is_prime(n)


def pollards_rho_factor(n):
    # Factorizes a number using Pollard's Rho Algorithm.
    x, y = 2, 5
    g = ma.gcd(abs(x - y), n)
    while g == 1:
        x = (x ** 2 + 1) % n
        y = ((y ** 2 + 1) ** 2 + 1) % n
        g = ma.gcd(abs(x - y), n)
        if g == n:
            return -1
    return g


def find_factors(n):
    # Finds two non-trivial factors of n.
    factor = pollards_rho_factor(n)
    if factor == -1:
        return -1, -1
    return factor, n // factor


def smallest_prime_factor(n):
    # Finds the smallest prime factor of n.
    if n in [1, 2, 5]: return n
    return pollards_rho_factor(n)


def all_prime_factors(n):
    # Finds all prime factors of n.
    factors = []
    while n > 1 and not is_prime(n):
        factor = smallest_prime_factor(n)
        factors.append(factor)
        n //= factor
    if n > 1: factors.append(n)
    return factors


def primitive_root_search(p):
    # Searches for a primitive root modulo p.
    factors = all_prime_factors(p - 1)
    for _ in range(10):
        candidate = random.randint(2, p - 1)
        if all(ma.fast_exponent(candidate, (p - 1) // factor, p) != 1 for factor in factors):
            return candidate
    return -1


def is_primitive_root(num, p):
    # Checks if a number is a primitive root modulo p.
    factors = all_prime_factors(p - 1)
    return all(ma.fast_exponent(num, (p - 1) // factor, p) != 1 for factor in factors)
