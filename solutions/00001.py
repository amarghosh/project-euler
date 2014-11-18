#!/usr/bin/python

def bruteforce():
    s = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            s += i
    print s
    return s

def usemath(a, b, top):
    def get_sum(x, t):
        x_ = t / x
        return x * (x_ * (x_ + 1)) / 2
    s_a = get_sum(a, top)
    s_b = get_sum(b, top)
    s_ab = get_sum(a*b, top)
    x = s_a + s_b - s_ab
    print x
    return x

if __name__ == '__main__':
    a = bruteforce()
    b = usemath(3, 5, 999)
    assert a == b
