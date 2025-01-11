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
s = {read() for _ in range(n)}
out = []
for _ in range(m):
    x = read()
    if x in s:
        out.append(x)

out.sort()
print(len(out))
print("\n".join(out))
