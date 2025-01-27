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

n = readInt()
grid = [list(readInts()) for _ in range(n)]

# dp[i][j] = 왼쪽 모서리가 i, j에 있는 경우의 수 [가로, 세로, 대각선]
# dp[i][j][0] = dp[i][j-1][0] + dp[i-1][j-1][2]
# dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j-1][2]
# dp[i][j][2] = dp[i][j-1][0] + dp[i-1][j][1]
dp = [[[0] * 3 for _ in range(n)] for _ in range(n)]
dp[0][0] = [1, 0, 0]

for i in range(n):
    for j in range(n):
        if i == 0 and j == 0:
            continue

        if j != n-1 and grid[i][j+1] == 0:
            dp[i][j][0] = dp[i][j-1][0] + dp[i-1][j-1][2]
        
        if i != n-1 and grid[i+1][j] == 0:
            dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j-1][2]
        
        if i != n-1 and j != n-1 and grid[i][j+1] == 0 and grid[i+1][j] == 0 and grid[i+1][j+1] == 0:
            dp[i][j][2] = dp[i][j-1][0] + dp[i-1][j][1] + dp[i-1][j-1][2]

print(dp[n-2][n-2][2] + dp[n-2][n-1][1] + dp[n-1][n-2][0])