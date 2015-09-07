#!/usr/bin/python

import math

def isprime(n):
    if n % 2 == 0:
        return False
    i = 3
    while i*i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def generate_primes_upto(max_val):
    p = [2]
    n = 3
    while n <= max_val:
        flag = True
        cutoff = int(math.sqrt(n))
        for i in p:
            if i > cutoff:
                break
            if n % i == 0:
                flag = False
                break
        if flag:
            p.append(n)
        n += 2
    return p


def get_prime_factors(num):
    facts = []
    max_fact = int(math.sqrt(num))
    while num % 2 == 0:
        facts.append(2)
        num /= 2
    i = 3
    while i <= max_fact:
        if num == 1:
            break
        if num%i == 0:
            while num != 1 and num%i == 0:
                facts.append(i)
                num /= i
        i += 2
    if num != 1:
        facts.append(num)
    return facts


def get_prime_factors_dict(num):
    factors = get_prime_factors(num)
    d = dict((f, 0) for f in factors)
    for i in d:
        d[i] = len(filter(lambda k: k == i, factors))
    return d


if __name__ == '__main__':
    pass
