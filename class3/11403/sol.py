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
grid = [list(readInts()) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if grid[i][k] == grid[k][j] == 1:
                grid[i][j] = 1

for l in grid:
    print(*l)
