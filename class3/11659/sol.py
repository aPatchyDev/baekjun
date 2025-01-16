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
sums = [0]
for k in readInts():
    sums.append(sums[-1] + k)

for _ in range(m):
    i, j = readInts()
    print(sums[j] - sums[i - 1])
