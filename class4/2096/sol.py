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

# dp[i][j] = i번째에서 j칸을 선택했을 때의 최대 점수
# dp[i][j] = max(dp[i-1][k] for k in j-1~j+1 and 0 <= k < 3) + num[i][j]
# Reuse grid as dp matrix

n = readInt()
big = [list(readInts()) for _ in range(n)]
small = [x.copy() for x in big]
for i in range(1, n):
    big[i][0] += max(big[i - 1][0], big[i - 1][1])
    big[i][1] += max(big[i - 1])
    big[i][2] += max(big[i - 1][1], big[i - 1][2])
    small[i][0] += min(small[i - 1][0], small[i - 1][1])
    small[i][1] += min(small[i - 1])
    small[i][2] += min(small[i - 1][1], small[i - 1][2])

print(max(big[n - 1]), min(small[n - 1]))