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

# Greedy 불가

n = readInt()
tri = [list(readInts()) for _ in range(n)]

# dp[i][j] = tri[i][j]까지 오는 max acc sum
# dp <- tri
for i in range(1, n):
    tri[i][0] += tri[i - 1][0]
    tri[i][i] += tri[i - 1][i - 1]
    for j in range(1, i):
        tri[i][j] += max(tri[i - 1][j], tri[i - 1][j - 1])

print(max(tri[n - 1]))
