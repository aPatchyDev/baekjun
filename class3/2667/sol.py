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

n = readInt()
grid = [int(read(), 2) for _ in range(n)]

groups = []
for i in range(n):
    for j in range(n):
        if (grid[i] >> j) & 1 == 0:
            continue

        cnt = 0
        stk = [(i, j)]
        while len(stk) > 0:
            x, y = stk.pop()
            if not (0 <= x < n and 0 <= y < n):
                continue
            if (grid[x] >> y) & 1 == 0:
                continue

            cnt += 1
            grid[x] ^= 1 << y
            stk.append((x - 1, y))
            stk.append((x + 1, y))
            stk.append((x, y - 1))
            stk.append((x, y + 1))

        groups.append(cnt)

groups.sort()
print(len(groups))
for x in groups:
    print(x)
