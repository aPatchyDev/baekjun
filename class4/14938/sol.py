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

n, m, r = readInts()
items = list(readInts())
paths = [[1 << 30] * n for _ in range(n)]
for i in range(n):
    paths[i][i] = 0

for _ in range(r):
    a, b, l = readInts()
    paths[a - 1][b - 1] = paths[b - 1][a - 1] = l

for k in range(n):
    for i in range(n):
        for j in range(n):
            if paths[i][j] > paths[i][k] + paths[k][j]:
                paths[i][j] = paths[i][k] + paths[k][j]

res = 0
for i in range(n):
    cnt = 0
    for j in range(n):
        if paths[i][j] <= m:
            cnt += items[j]

    if cnt > res:
        res = cnt

print(res)
