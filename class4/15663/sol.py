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

from itertools import permutations

_, m = readInts()
nums = list(readInts())
nums.sort()
prevs = set()
for p in permutations(nums, m):
    if p not in prevs:
        prevs.add(p)
        print(*p)
