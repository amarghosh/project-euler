#!/usr/bin/env python

def ispalindrome(s):
    length = len(s)
    for i in range(length/2):
        if s[i] != s[length - 1 - i]:
            return False
    return True

