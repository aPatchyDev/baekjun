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

# 거리가 1이므로 BFS가 가능하다

from collections import deque

n, m = readInts()
grid = [list(readInts()) for _ in range(n)]
sx = sy = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            grid[i][j] = -1
        elif grid[i][j] == 2:
            sx = i
            sy = j
            grid[i][j] = 0

que = deque()
offs = (-1, 0), (1, 0), (0, -1), (0, 1)
for x, y in offs:
    que.append((1, sx + x, sy + y))

while len(que) > 0:
    d, x, y = que.popleft()
    if not (0 <= x < n and 0 <= y < m) or 0 < grid[x][y] <= d or grid[x][y] == 0:
        continue

    grid[x][y] = d
    for i, j in offs:
        que.append((d + 1, x + i, y + j))

for row in grid:
    print(*row)
