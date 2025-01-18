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

sys.setrecursionlimit(10**6)

n, m = readInts()
grid = [list(read()) for _ in range(n)]

for x, r in enumerate(grid):
    for y, c in enumerate(r):
        if c == "I":
            break
    else:
        continue
    break

def sol(i, j):
    if not (0 <= i < n and 0 <= j < m):
        return 0

    old = grid[i][j]
    if old == "X":
        return 0

    grid[i][j] = "X"
    cnt = 1 if old == "P" else 0
    return cnt + sol(i - 1, j) + sol(i + 1, j) + sol(i, j - 1) + sol(i, j + 1)

res = sol(x, y)
print("TT" if res == 0 else res)
