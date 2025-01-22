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
grid = [list(readInts()) for _ in range(n)]

offsets = [
    [[0, 1], [0, 2], [0, 3]],   # I
    [[0, 1], [1, 0], [1, 1]],   # []
    [[0, 1], [0, 2], [1, 1]],   # ㅜ
    [[0, 1], [0, 2], [1, 2]],   # L
    [[1, 0], [2, 0], [2, 1]],   # L
    [[0, 1], [1, 0], [1, -1]],  # N
    [[0, -1], [1, 0], [1, 1]]   # N
]

big = 0
for i in range(4):
    if i != 0:
        # Rotate offsets by 90 deg
        for off in offsets:
            for i in range(3):
                off[i][0], off[i][1] = -off[i][1], off[i][0]

    for x in range(n):
        for y in range(m):
            for off in offsets:
                tot = grid[x][y]
                for i, j in off:
                    if not (0 <= x + i < n and 0 <= y + j < m):
                        break
                    tot += grid[x + i][y + j]
                else:
                    big = max(big, tot)

print(big)
