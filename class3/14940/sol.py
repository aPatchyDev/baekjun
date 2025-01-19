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

# 무방향 그래프이므로 목적지에서 출발하는 SSSP를 돌리면 된다

n, m = readInts()
grid = [list(readInts()) for _ in range(n)]
sx = sy = 0
for i in range(n):
    for j in range(m):
        if grid[i][j] == 1:
            grid[i][j] = 1_000_000
        elif grid[i][j] == 2:
            sx = i
            sy = j
            grid[i][j] = 0

import heapq
pq = [(1, sx - 1, sy), (1, sx + 1, sy), (1, sx, sy - 1), (1, sx, sy + 1)]
heapq.heapify(pq)
while len(pq) > 0:
    d, x, y = heapq.heappop(pq)
    if not (0 <= x < n and 0 <= y < m) or d == 0 or d >= grid[x][y]:
        continue

    grid[x][y] = d
    heapq.heappush(pq, (d + 1, x - 1, y))
    heapq.heappush(pq, (d + 1, x + 1, y))
    heapq.heappush(pq, (d + 1, x, y - 1))
    heapq.heappush(pq, (d + 1, x, y + 1))

for row in grid:
    print(*(x if x != 1_000_000 else -1 for x in row))
