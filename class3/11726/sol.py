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

# n을 1, 2의 합으로 표현하는 방법과 동일
# n = 2 x k + 1 x n-2k for k in range(n // 2)

n = readInt()

import math
print(sum(math.comb(n - k, k) for k in range(n // 2 + 1)) % 10007)
