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

import re
tokens = re.split(r"(\+|-)", read())
ids = list(map(lambda x: -1 if x == "-" else 1 if x == "+" else int(x), tokens))
n = len(ids) // 2 + 1

# 괄호로 ids[2i:2j + 1]를 묶은 식의 결과값을 dp[i][j]로 정의
# ids[2k]: 숫자, ids[2k + 1]: +1/-1
# dp[i][j] = min/max of dp[i][k] +/- dp[k + 1][j] for i= < k < j
# if k == i: (a) + (b + ...)
# if k == j - 1: (a + ...) + (b) == (a + ... + b)

dp = [[None] * n for _ in range(n)]
for i in range(0, n):
    dp[i][i] = ids[2 * i]

for o in range(1, n):
    for i in range(n - o):
        j = i + o

        if i > 0 and ids[2 * i - 1] < 0:
            dp[i][j] = max(dp[i][k] + ids[2 * k + 1] * dp[k + 1][j] for k in range(i, j))
        else:
            dp[i][j] = min(dp[i][k] + ids[2 * k + 1] * dp[k + 1][j] for k in range(i, j))

print(dp[0][-1])
