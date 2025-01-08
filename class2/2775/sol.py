#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

dp = { (0, i): i for i in range(1, 15) }

def f(a, b):
    if b == 1:
        return 1
    if (a, b) not in dp:
        dp[ (a, b) ] = f(a, b - 1) + f(a - 1, b)

    return dp[ (a, b) ]

for _ in range(readInt()):
    k = readInt()
    n = readInt()

    print(f(k, n))
