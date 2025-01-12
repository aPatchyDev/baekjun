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

# DP solution
# Cnt(x) = 1 + min(Cnt(x / 3), Cnt(x / 2), Cnt(x - 1) for possible values)

n = readInt()

cnt = [0] * (n + 2)
for i in range(2, n + 1):
    cnt[i] = cnt[i - 1] + 1
    if i % 2 == 0:
        cnt[i] = min(cnt[i], cnt[i // 2] + 1)
    if i % 3 == 0:
        cnt[i] = min(cnt[i], cnt[i // 3] + 1)

print(cnt[n])
