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

# dp[n][w] = objs[:n] 중에 sum(weight) <= w인 최대 가치
# = if objs[n].weight > w: dp[n-1][w]
#   else: max(dp[n-1][:w-objs[n].weight] + objs[n].weight, dp[n-1][w])

n, k = readInts()
objs = [list(readInts()) for _ in range(n)]

dp = [0] * (k + 1)
for w, v in objs:
    for i in range(k, 0, -1):
        if w <= i:
            dp[i] = max(dp[i-w] + v, dp[i])

print(dp[-1])