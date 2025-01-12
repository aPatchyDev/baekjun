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
pw = dict(read().split() for _ in range(n))
for _ in range(m):
    print(pw[read()])
