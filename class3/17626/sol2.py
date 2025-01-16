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

n = readInt()

dp = [100_000] * 50_002
for i in range(224):
    dp[i * i] = 1

for i in range(2, n + 1):
    x = min(dp[k * k] + dp[i - k * k] for k in range(1, int(i ** 0.5) + 1))
    dp[i] = min(dp[i], x)

print(dp[n])
