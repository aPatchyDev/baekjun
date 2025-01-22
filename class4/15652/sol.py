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

from itertools import combinations_with_replacement

n, m = readInts()
for s in combinations_with_replacement(range(1, n + 1), m):
    print(*s)
