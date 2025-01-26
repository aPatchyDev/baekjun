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

# lcs[i][j] = length of LCS between a[:i+1], b[:j+1]

a = read()
b = read()
n = len(a)
m = len(b)

lcs = [[0] * m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if a[i] == b[j]:
            if j == 0:
                lcs[i][j] = 1
            else:
                lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i][j-1], lcs[i-1][j])

print(lcs[-1][-1])