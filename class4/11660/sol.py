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

# Make grid store sum from 1,1 to x, y

n, m = readInts()
grid = [[0] * (n + 1)] + [[0] + list(readInts()) for _ in range(n)]
for r in range(1, n + 1):
    for i in range(1, n + 1):
        grid[r][i] += grid[r][i - 1] + grid[r - 1][i] - grid[r - 1][i - 1]

for _ in range(m):
    x, y, i, j = readInts()
    tot = grid[i][j] + grid[x - 1][y - 1] - grid[i][y - 1] - grid[x - 1][j]

    print(tot)
