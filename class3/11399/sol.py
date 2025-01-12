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

# Select quickest person first
# p1 + (p1 + p2) + ... + (p1 + ... + pn)
# = p1 * n + p2 * (n-1) + ... + pn * 1

readInt()
pn = list(readInts())
pn.sort(reverse=True)
print(sum(v * (i + 1) for i, v in enumerate(pn)))
