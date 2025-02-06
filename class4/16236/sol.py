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

n = readInt()
grid = [[0] * n for _ in range(n)]
fish = [[] for _ in range(8)]
sharkx = sharky = 0
size = 2
for i in range(n):
    for j, k in enumerate(readInts()):
        if k == 9:
            sharkx = i
            sharky = j
        elif k > 0:
            grid[i][j] = k
            fish[k].append((i, j))

moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def check(dist, x, y, prev, i, j):
    if dist != prev:
        return dist < prev

    if x != i:
        return x < i

    return y < j

time = 0
eat = 0
while True:
    # Compute distance to each square
    dist = [[1 << 30] * n for _ in range(n)]
    dist[sharkx][sharky] = 0
    que = deque()
    que.append((sharkx, sharky))
    while len(que) != 0:
        x, y = que.popleft()
        for dx, dy in moves:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if dist[nx][ny] == 1 << 30 and grid[nx][ny] <= size:
                dist[nx][ny] = dist[x][y] + 1
                que.append((nx, ny))

    # Find target fish
    d = 1 << 30
    tx, ty = -1, -1
    for pos in fish[1:size]:
        for x, y in pos:
            if check(dist[x][y], x, y, d, tx, ty):
                tx, ty = x, y
                d = dist[x][y]

    # Eat fish
    if d != 1 << 30:
        time += d
        sharkx, sharky = tx, ty
        tsize = grid[tx][ty]
        fish[tsize].remove((tx, ty))
        grid[tx][ty] = 0
        eat += 1
        if eat == size:
            eat = 0
            size += 1
    else:
        break

print(time)
