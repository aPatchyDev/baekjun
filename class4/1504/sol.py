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

n, e = readInts()
dists = [[2 << 30] * (n+1) for _ in range(n+1)]
for _ in range(e):
    a, b, c = readInts()
    dists[a][b] = c
    dists[b][a] = c
for i in range(1, n + 1):
    dists[i][i] = 0

a, b = readInts()
for k in range(1, n+1):
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dists[i][j] > dists[i][k] + dists[k][j]:
                dists[i][j] = dists[i][k] + dists[k][j]

res = min(dists[1][a] + dists[a][b] + dists[b][n],
          dists[1][b] + dists[b][a] + dists[a][n]
          )
print(res if res < (2 << 30) else -1)