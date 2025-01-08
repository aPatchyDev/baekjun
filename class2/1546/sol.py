#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n = readInt()
nums = list(readInts())
k = max(nums) * n

# E(a * X) = a * E(x)
print(sum(nums) * 100 / k)
