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
grid = [list(read()) for _ in range(n)]

stk = []
for x, r in enumerate(grid):
    for y, c in enumerate(r):
        if c == "I":
            stk.append((x, y))
            break

cnt = 0
while len(stk) > 0:
    i, j = stk.pop()
    if not (0 <= i < n and 0 <= j < m):
        continue

    old = grid[i][j]
    grid[i][j] = "X"
    match old:
        case "X":
            continue
        case "P":
            cnt += 1

    stk.append((i - 1, j))
    stk.append((i + 1, j))
    stk.append((i, j - 1))
    stk.append((i, j + 1))

print("TT" if cnt == 0 else cnt)

# Almost x7 faster to implement DFS by stack than recursion
