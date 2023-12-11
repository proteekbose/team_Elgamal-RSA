# Modular Arithmetic Tools for Crypto-systems

# Check if a number is odd
isOdd = lambda val: val % 2 != 0

# Euclidean algorithm for GCD (The Greatest Common Divisor)
gcd = lambda m, n: abs(m) if n == 0 else gcd(n, m % n)


# Multiplicative inverse algorithm
def multiplicative_inverse(x, modulus):
    # Finding multiplicative inverse of x under modulus.
    for y in range(1, modulus):
        if (x * y) % modulus == 1:
            return y
    return -1


# Fast Exponentiation Algorithm
def fast_exponent(base, exponent, modulus):
    # Efficiently computing (base^exponent) % modulus.
    result = 1
    base = base % modulus

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent % 2:
            result = (result * base) % modulus

        # exponent must be even now
        exponent >>= 1
        base = (base * base) % modulus

    return result


# Extended Euclidean Algorithm
def extended_gcd(a, b):
    # Extended Euclidean Algorithm to find coefficients of Bezout's identity.
    if a == 0:
        return b, 0, 1

    gcd_ext, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd_ext, x, y
