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

n = readInt()
nums = [(v, i) for i, v in enumerate(readInts())]
out = [0] * n

nums.sort()
i = 0
prev = nums[0][0]
for v, k in nums:
    if prev < v:
        i += 1

    out[k] = i
    prev = v

print(" ".join(map(str, out)))

# nums.sort() is O(nlogn)
# Looping over nums is O(n)
# Runtime near constant regardless of data distribution
