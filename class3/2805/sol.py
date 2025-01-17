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

n, m = readInts()
trees = list(readInts())

hi = max(trees)
lo = 0
while lo + 1 < hi:
    mid = (lo + hi) // 2
    res = sum(t - mid for t in trees if t > mid)

    if res < m:
        hi = mid
    else:
        lo = mid

print(lo)
