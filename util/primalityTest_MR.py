# Miller-Rabin Primality Test Implementation
from util import modularArithmetic as ma
from util import pseudorandomGenerator_BBS as pg_BBS
from util import pseudorandomGenerator_NR as pg_NR
import random


# Check if a number is prime using Miller-Rabin Test
def is_prime(n):
    # Checking if a number is prime using the Miller-Rabin primality test.
    r, m = 0, n - 1
    while m % 2 == 0:  # Decompose n-1 as 2^r * m
        m //= 2
        r += 1

    b = random.randint(1, n - 1)
    for k in range(r):
        exponent = m if k == 0 else (2 ** k) * m
        result = ma.fast_exponent(b, exponent, n)
        if result in [1, -1 % n]:
            return True
    return False


# Generate an array of prime numbers
def get_primes(count, rand_method):
    # Generates an array of prime numbers using specified random number generator.
    primes = []
    while count > 0:
        num = random.randint(1000, 10000) if rand_method == 0 else \
            pg_NR.rand_gen() if rand_method == 1 else \
                pg_BBS.rand_gen() if rand_method == 2 else None
        if num is None: return primes

        num += 1 if num % 2 == 0 else 0
        if all(is_prime(num) for _ in range(3)):
            primes.append(num)
            count -= 1
    return primes


# Compute modulus from two primes
def get_modulus(count, rand):
    # Get modulus by multiplying two prime numbers.
    primes = get_primes(count, rand)
    return primes[0] * primes[1], primes[0], primes[1]



# b= is_prime(302972288202616367311)
# print(b)