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

# Floyd Warshall solution
# Floyd Warshall (DP): O(V^3)

n, m = readInts()
dp = [[n] * n for _ in range(n)]
for _ in range(m):
    a, b = readInts()
    dp[a - 1][b - 1] = dp[b - 1][a - 1] = 1

for i in range(n):
    dp[i][i] = 0

for k in range(n):
    for i in range(n):
        for j in range(n):
            dp[i][j] = min(dp[i][j], dp[i][k] + dp[k][j])

res = 0
score = 100_000
for i in range(n):
    tot = sum(dp[i])
    if tot < score:
        score = tot
        res = i + 1

print(res)

# N이 충분히 작아서 cache miss가 적은 Floyd Warshall이 더 빠르게 나온 듯
