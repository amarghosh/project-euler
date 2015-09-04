#!/usr/bin/python

def main():
    prev = 1
    fib = 2
    res = 0
    MAX = 4 * (10**6)
    while fib <= MAX:
        if fib % 2 == 0:
            res += fib
        t = fib
        fib += prev
        prev = t
    return res


if __name__ == '__main__':
    print main()
