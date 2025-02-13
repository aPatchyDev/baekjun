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

n, s = readInts()
nums = list(readInts())
nums.append(0)  # Prevent index error

lo = hi = 0
tot = nums[0]
dist = 1 << 20
while hi < n:
    if tot < s:
        hi += 1
        tot += nums[hi]
    else:
        dist = min(dist, hi - lo)
        tot -= nums[lo]
        lo += 1

if dist == 1 << 20:
    print(0)
else:
    print(dist + 1)
