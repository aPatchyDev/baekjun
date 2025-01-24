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

# cost(n, color) = n번째를 color로 칠할 때 1~n을 칠한 총 비용
# = min(cost(n - 1, x) + price[color] for x != color)

n = readInt()
prices = [list(readInts()) for _ in range(n)]

costs = [[0] * 3 for _ in range(n)]
costs[0] = prices[0]
for i in range(1, n):
    for j in range(3):
        costs[i][j] = min(costs[i-1][j-1], costs[i-1][j-2]) + prices[i][j]

print(min(costs[n - 1]))
