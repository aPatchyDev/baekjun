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

m, n, h = readInts()
tower = []
tomatos = deque()
for z in range(h):
    floor = []
    for y in range(n):
        row = list(readInts())
        floor.append(row)
        for x, k in enumerate(row):
            if k == 1:
                tomatos.append((z, y, x))
                row[x] = 0
            elif k == 0:
                row[x] = 10_000_000

    tower.append(floor)

offs = ((-1, 0, 0), (1, 0, 0), (0, -1, 0), (0, 1, 0), (0, 0, -1), (0, 0, 1))
while len(tomatos) > 0:
    z, y, x = tomatos.popleft()
    for off in offs:
        a, b, c = off
        i, j, k = z + a, y + b, x + c
        if not (0 <= i < h) or not (0 <= j < n) or not (0 <= k < m):
            continue

        if tower[i][j][k] == 10_000_000:
            tower[i][j][k] = tower[z][y][x] + 1
            tomatos.append((i, j, k))

d = 0
for i in range(h):
    for j in range(n):
        for k in range(m):
            d = max(d, tower[i][j][k])
            if d == 10_000_000:
                print(-1)
                exit()

print(d)
