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
grid = []
virus = []
for i in range(n):
    grid.append(list(readInts()))
    for j, k in enumerate(grid[-1]):
        if k == 2:
            virus.append((i, j))

def cnt(walls):
    cpy = [x.copy() for x in grid]
    stk = virus.copy()
    offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while len(stk) != 0:
        x, y = stk.pop()

        for i, j in offsets:
            if 0 <= x + i < n and 0 <= y + j < m:
                if cpy[x + i][y + j] == 0 and (x + i, y + j) not in walls:
                    cpy[x + i][y + j] = 2
                    stk.append((x + i, y + j))

    cnt = -3
    for row in cpy:
        for x in row:
            if x == 0:
                cnt += 1

    return cnt

def sol(walls):
    if len(walls) == 3:
        return cnt(walls)

    if len(walls) == 0:
        x = y = 0
    else:
        x = walls[-1][0]
        y = walls[-1][1] + 1

    res = 0
    for i in range(x, n):
        while y < m:
            if grid[i][y] == 0:
                res = max(res, sol(walls + [(i, y)]))
            y += 1

        y = 0

    return res

print(sol([]))
