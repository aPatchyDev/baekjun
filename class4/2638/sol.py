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
grid = [[0] * m for _ in range(n)]
cheese = set()
for i in range(n):
    for j, k in enumerate(readInts()):
        grid[i][j] = k
        if k == 1:
            cheese.add((i, j))

outside = [[0] * m for _ in range(n)]
moves = ((-1, 0), (1, 0), (0, -1), (0, 1))

def flood(x, y):
    stk = [(x, y)]
    while len(stk) != 0:
        i, j = stk.pop()
        outside[i][j] = 1
        for di, dj in moves:
            nx = i + di
            ny = j + dj
            if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] == 0 and outside[nx][ny] == 0:
                outside[nx][ny] = 1
                stk.append((nx, ny))

flood(0, 0)

time = 0
while len(cheese) != 0:
    melt = []
    for x, y in cheese:
        exposed = 0
        for dx, dy in moves:
            exposed += outside[x+dx][y+dy]

        if exposed >= 2:
            melt.append((x, y))

    if len(melt) != 0:
        time += 1
        cheese.difference_update(melt)
        for x, y in melt:
            grid[x][y] = 0
            flood(x, y)

print(time)
