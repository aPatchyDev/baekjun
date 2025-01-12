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

# 동전은 이전 동전의 배수라는 입력 조건 때문에 greedy 가능

n, val = readInts()
coins = [readInt() for _ in range(n)]

cnt = 0
for c in reversed(coins):
    q, val = divmod(val, c)
    cnt += q

print(cnt)
