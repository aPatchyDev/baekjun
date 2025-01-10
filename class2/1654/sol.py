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

k, n = readInts()
cables = [readInt() for _ in range(k)]

# 이론상 최대: sum(cables) // n
# ...의 범위: 2^31 x 10,000 // 1,000,000 ~= 2,200,000,000 // 100 ~= 22,000,000
# 주어진 길이가 가능한지 테스트: sum(e // l for e in cables)
# ...의 실행횟수 범위: 10,000
# 10,000 x O(fn(22,000,000)) ~= 100,000,000 ops/s x 2s
# O(fn(22,000,000)) ~= 20,000
# If fn(n) = n: fn(22,000,000) >>> 20,000
# If fn(n) = log2(n): fn(22,000,000) ~= 25

lo = 1  # if set to 0, can cause division by zero (ex: 2 3 / 1 / 2)
hi = sum(cables) // n
while lo < hi:
    l = (lo + hi) >> 1
    cnt = sum(e // l for e in cables)
    if cnt >= n:
        lo = l + 1
    else:
        hi = l - 1

if sum(e // lo for e in cables) >= n:
    print(lo)
else:
    print(lo - 1)
