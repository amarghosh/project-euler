#!/usr/bin/python

# Print a*b*c where a,b,c forms a pythagorian triplet and a+b+c = 1000

def solve():
    s = 1000
    for a in range(1, s):
        a2 = a*a
        for b in range(a+1, s):
            c = s - (a+b)
            if a*a + b*b == c*c:
                print a,b,c
                return a*b*c

print solve()

