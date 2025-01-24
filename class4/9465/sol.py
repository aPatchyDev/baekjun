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

for _ in range(readInt()):
    n = readInt()
    dp = [[0] * n]
    dp.append(list(readInts()))
    dp.append(list(readInts()))
    for i in range(1, n):
        dp[0][i] += max(dp[1][i - 1], dp[2][i -1])
        dp[1][i] += max(dp[0][i - 1], dp[2][i - 1])
        dp[2][i] += max(dp[0][i - 1], dp[1][i - 1])


    print(max(dp[0][n - 1], dp[1][n - 1], dp[2][n - 1]))
