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

for _ in range(readInt()):
    m, n, k = readInts()
    grid = [[0] * n for _ in range(m)]
    points = []
    for _ in range(k):
        x, y = readInts()
        grid[x][y] = 1
        points.append((x, y))

    stk = []
    cnt = 0
    for p in points:
        if grid[p[0]][p[1]] == 0:
            continue

        stk.append(p)
        cnt += 1
        while len(stk) > 0:
            x, y = stk.pop()
            if 0 <= x < m and 0 <= y < n and grid[x][y] == 1:
                grid[x][y] = 0
                stk.append((x - 1, y))
                stk.append((x + 1, y))
                stk.append((x, y - 1))
                stk.append((x, y + 1))

    print(cnt)
