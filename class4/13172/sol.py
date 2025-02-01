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

res = 0
for _ in range(readInt()):
    n, s = readInts()
    res = (res + s * pow(n, -1, 1_000_000_007)) % 1_000_000_007

print(res)
