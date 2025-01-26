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

n, k = readInts()
times = dict()

if k <= n:
    print(n - k)
    exit()

import heapq
pq = [(0, n)]
while len(pq) != 0:
    t, x = heapq.heappop(pq)
    if x < 0 or (x in times and times[x] <= t):
        continue
    if x == k:
        print(t)
        break

    times[x] = t
    if k <= x:
        heapq.heappush(pq, (x - k + t, k))
    else:

        heapq.heappush(pq, (t + 1, x - 1))
        heapq.heappush(pq, (t + 1, x + 1))
        heapq.heappush(pq, (t, 2 * x))

# 더 빠른 풀이는 PQ 대신 Queue를 쓰는 SPFA 사용