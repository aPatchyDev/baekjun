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

r, c = readInts()
grid = [[ord(c) - 65 for c in read()] for _ in range(r)]
masks = [1 << i for i in range(26)]

offsets = [(-1, 0), (1, 0), (0, -1), (0, 1)]
stk = [(0, 0, masks[grid[0][0]], 1)]
res = 1
while len(stk) != 0:
    x, y, visited, cnt = stk.pop()
    res = max(res, cnt)
    for ox, oy in offsets:
        i, j = x + ox, y + oy
        if 0 <= i < r and 0 <= j < c and (visited & masks[grid[i][j]]) == 0:
            stk.append((i, j, visited | masks[grid[i][j]], cnt + 1))

print(res)

# 추가 최적화 방법 (일부 데이터에 한해서)
# dp(coord, bitmask)의 결과를 저장하면 탐색 범위를 더 줄일 수 있다