#!/usr/bin/python

# smallest positive number that is evenly divisible by all of the numbers from 1 to 20

from num_utils import *

def solve(x):
    factors = {}
    for num in range(2, x + 1):
        f = get_prime_factors_dict(num)
        for i in f:
            if i not in factors:
                factors[i] = 1
                continue
            factors[i] = max(factors[i], f[i])
    res = 1
    for i in factors:
        res *= (i ** factors[i])
    return res

print solve(20)

