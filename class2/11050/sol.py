#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n, k = readInts()

up = 1
for i in range(n, n - k, -1):
    up *= i

down = 1
for i in range(1, k + 1):
    down *= i

print(up // down)
