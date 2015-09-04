#!/usr/bin/python

# largest prime factor

from num_utils import *

def solve(N):
    facts = get_prime_factors(N)
    return facts[-1]

X = 600851475143
m = solve(X)
print m

