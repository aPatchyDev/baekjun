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

# n-2에서 2x2 추가한 경우 1개 + n-1에서 2x1 추가한 경우 1개
# dp[n] = dp[n-2] + dp[n-1]
# 피보나치..?
# dp[1] = 1
# dp[2] = 2
# dp[3] = 3

n = readInt()

if n < 4:
    print(n)
else:
    a, b = 1, 2
    for _ in range(n - 2):
        a, b = b, a + b

    print(b % 10007)
