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
grid = [list(read()) for _ in range(n)]
offs = [[-1, 0], [1, 0], [0, -1], [0, 1]]

def dfs(chset):
    visit = [0] * n
    cnt = 0
    for x in range(n):
        for y in range(n):
            if visit[x] & (1 << y) != 0:
                    continue

            cnt += 1
            stk = [(x, y)]
            chs = [ch for ch in chset if grid[x][y] in ch][0]
            while len(stk) > 0:
                i, j = stk.pop()
                if visit[i] & (1 << j) != 0:
                    continue
                if grid[i][j] not in chs:
                    continue

                visit[i] |= (1 << j)
                for off in offs:
                    a, b = off
                    a += i
                    b += j
                    if 0 <= a < n and 0 <= b < n:
                        stk.append((a, b))

    return cnt

print(dfs(["R", "G", "B"]), dfs(["RG", "B"]))
