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

# Minor optimization

n = readInt()
prices = [list(readInts()) for _ in range(n)]

for i in range(1, n):
    prices[i][0] += min(prices[i - 1][1], prices[i - 1][2])
    prices[i][1] += min(prices[i - 1][0], prices[i - 1][2])
    prices[i][2] += min(prices[i - 1][0], prices[i - 1][1])

print(min(prices[n - 1]))
