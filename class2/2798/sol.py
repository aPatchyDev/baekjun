#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n, m = readInts()
nums = list(readInts())

import itertools

s = 0
for c in itertools.combinations(nums, 3):
    k = sum(c)
    if k == m:
        s = k
        break
    elif k < m and k > s:
        s = k

print(s)
