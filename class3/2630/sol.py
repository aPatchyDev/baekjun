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
grid = [list(readInts()) for _ in range(n)]

def sol(x, y, k):
    # x, y부터 한 변이 k인 영역에 필요한 종이 수
    if k == 1:
        return (1, 0) if grid[x][y] == 0 else (0, 1)

    k = k // 2
    parts = [sol(x, y, k), sol(x, y + k, k), sol(x + k, y, k), sol(x + k, y + k, k)]
    white = sum(p[0] for p in parts)
    blue = sum(p[1] for p in parts)
    if white == 4 and blue == 0:
        return 1, 0
    elif white == 0 and blue == 4:
        return 0, 1
    else:
        return white, blue

print(*sol(0, 0, n), sep="\n")
