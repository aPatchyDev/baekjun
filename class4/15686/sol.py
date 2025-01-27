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

# 치킨거리 계산: 집 2n개마다 치킨집 <14까지의 맨해튼 거리 중 최솟값 ~= 10^3
# 치킨집 n개 중 m개 선택: min(O(n^m), O(2^n)) = O(2^13) ~= 10^4
# < 10^8이므로 bruteforce

n, m = readInts()
shops = []
houses = dict()
for i in range(n):
    for j, c in enumerate(readInts()):
        if c == 1:
            houses[i, j] = []
        elif c == 2:
            shops.append((i, j))

# Precompute per-house distance
for coord, lst in houses.items():
    x, y = coord
    for i, j in shops:
        lst.append(abs(x - i) + abs(y - j))

from itertools import combinations

res = 2 << 30
for s in combinations(range(len(shops)), m):
    city = 0
    for dist in houses.values():
        city += min(dist[i] for i in s)
    
    res = min(res, city)

print(res)