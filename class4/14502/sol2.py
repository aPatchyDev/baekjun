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

from itertools import combinations

n, m = readInts()
grid = []
virus = []
empty = []
for i in range(n):
    grid.append(list(readInts()))
    for j, k in enumerate(grid[-1]):
        if k == 2:
            virus.append((i, j))
        elif k == 0:
            empty.append((i, j))

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


res = 0
for choice in combinations(empty, 3):
    res = max(cnt(choice), res)

print(res)

# Iterating over combination of empty cells is faster
# than finding empty cells in a loop
