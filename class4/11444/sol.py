#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

import math
def round(n):
    return math.floor(n + 0.5)

# [Fn, Fn-1]    = [Fn-1, Fn-2] x [1, 1] = [1, 1] ^ (n-1)
# [Fn-1, Fn-2]    [Fn-2, Fn-3]   [1, 0]   [1, 0]

n = readInt()
if n == 1 or n == 2:
    print(1)
else:
    # Matrix to square
    a = b = c = 1
    d = 0

    # Identity matrix
    e = h = 1
    f = g = 0
    n -= 1
    while n > 0:
        if n & 1 == 1:
            e, f, g, h = a*e+c*f, b*e+d*f, a*g+c*h, b*g+d*h
            e %= 1_000_000_007
            f %= 1_000_000_007
            g %= 1_000_000_007
            h %= 1_000_000_007

        a, b, c, d = a*a + b*c, a*b+b*d, a*c+c*d, b*c+d*d
        a %= 1_000_000_007
        b %= 1_000_000_007
        c %= 1_000_000_007
        d %= 1_000_000_007

        n >>= 1

    print(e)
