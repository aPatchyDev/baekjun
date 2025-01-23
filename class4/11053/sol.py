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
nums = list(readInts())

cnts = [1] * n
for i, k in enumerate(nums):
    for j in reversed(range(i)):
        if nums[j] < k:
            cnts[i] = max(1 + cnts[j], cnts[i])

print(max(cnts))
