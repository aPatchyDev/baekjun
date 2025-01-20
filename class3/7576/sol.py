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

from collections import deque

m, n = readInts()
grid = []
que = deque()
for x in range(n):
    grid.append(list(readInts()))
    for y, k in enumerate(grid[x]):
        if k == 0:
            grid[x][y] = 10_000_000
        elif k == 1:
            grid[x][y] = 0
            que.append((x, y))

offs = ((-1, 0), (1, 0), (0, -1), (0, 1))
while len(que) > 0:
    x, y = que.popleft()
    for off in offs:
        a, b = off
        i, j = x + a, y + b
        if not (0 <= i < n and 0 <= j < m):
            continue

        if grid[i][j] == 10_000_000:
            grid[i][j] = grid[x][y] + 1
            que.append((i, j))

d = 0
for i in range(n):
    for j in range(m):
        d = max(d, grid[i][j])
        if d == 10_000_000:
            print(-1)
            exit()

print(d)
