#!/usr/bin/python

# largest palindrome number that is product of two three digit numbers

from str_utils import *

def bruteforce():
    res = 0
    x = 0
    y = 0
    for i in range(100, 1000):
        for j in range(100, 1000):
            if ispalindrome(str(i*j)):
                if i*j > res:
                    x = i
                    y = j
                    res = i*j
    print x, y
    return res


print bruteforce()
