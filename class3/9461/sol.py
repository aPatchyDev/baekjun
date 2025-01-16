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

# P(N | N < 4) = 1
# P(N | N > 3) = P(N - 5) + P(N - 1)

nums = [readInt() for _ in range(readInt())]
hi = max(nums)

p = [0, 1, 1, 1]
for i in range(4, hi + 1):
    p.append(p[i - 5] + p[i - 1])

for n in nums:
    print(p[n])
