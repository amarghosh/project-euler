#!/usr/bin/python

# What is the 10001st prime number?

import num_utils

def find_nth_prime(X):
    i = 1
    n = 1
    while i < X:
        n += 2
        while not num_utils.isprime(n):
            n += 2
        i += 1
    return n

def main():
    X = 10001
    print num_utils.generate_n_primes(X)[-1]
    # print find_nth_prime(X)

main()
