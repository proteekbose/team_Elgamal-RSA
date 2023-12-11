# Baby-step Giant-step Algorithm for Logarithm Problem
import math
from util import modularArithmetic as ma


def baby_giant_step(a, b, n):
    # Solves logarithm problem b^l ≡ a (mod n) to find l using Baby-step Giant-step Algorithm.
    m = math.ceil(math.sqrt(n - 1))  # Ceiling of square root of n-1

    # Baby-step: compute b^j for j in range m
    baby_steps = [(b ** j) % n for j in range(m)]

    # Compute inverse and constant for giant steps
    inv_b = ma.multiplicative_inverse(b, n)
    c = ma.fast_exponent(inv_b, m, n)

    # Giant-step: compute a * c^i for i in range m
    giant_steps = [(a * (c ** i)) % n for i in range(m)]

    # Find matching pair (k, h) where baby_step[k] == giant_step[h]
    for k, baby in enumerate(baby_steps):
        if baby in giant_steps:
            h = giant_steps.index(baby)
            return h * m + k

    return -1  # If no solution found
