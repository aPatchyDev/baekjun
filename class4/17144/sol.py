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

r, c, t = readInts()
grid = [list(readInts()) for _ in range(r)]
for pure in range(r):
    if grid[pure][0] == -1:
        break

offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
for _ in range(t):
    # Spread
    delta = [[0] * c for _ in range(r)]
    for x in range(r):
        for y in range(c):
            if grid[x][y] < 5:
                continue

            dust = grid[x][y] // 5
            for i, j in offsets:
                if not (0 <= x + i < r and 0 <= y + j < c):
                    continue
                if (x + i == pure or x + i == pure + 1) and y + j == 0:
                    continue

                delta[x][y] -= dust
                delta[x+i][y+j] += dust

    for x in range(r):
        for y in range(c):
            grid[x][y] += delta[x][y]

    # Purify
    for x in reversed(range(1, pure)):
        grid[x][0] = grid[x-1][0]
    for x in range(pure + 2, r-1):
        grid[x][0] = grid[x+1][0]

    for x in range(1, c):
        grid[0][x-1] = grid[0][x]
        grid[r-1][x-1] = grid[r-1][x]

    for x in range(pure):
        grid[x][c-1] = grid[x+1][c-1]
    for x in reversed(range(pure+2, r)):
        grid[x][c-1] = grid[x-1][c-1]

    for x in reversed(range(2, c)):
        grid[pure][x] = grid[pure][x-1]
        grid[pure+1][x] = grid[pure+1][x-1]

    grid[pure][1] = grid[pure+1][1] = 0

# Purifier -1 x 2
res = 2
for row in grid:
    for x in row:
        res += x

print(res)
