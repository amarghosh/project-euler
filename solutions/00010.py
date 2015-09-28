#!/usr/bin/python

import num_utils

def solve():
    p = num_utils.generate_primes_upto(2 * 10**6)
    s = 0
    for i in p:
        s += i
    print s

solve()

