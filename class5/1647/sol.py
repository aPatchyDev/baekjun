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

# Minimum Spanning Tree에서 최대 가중치 하나 제거하기

import heapq

n, m = readInts()
graph = [dict() for _ in range(n)]
for _ in range(m):
    a, b, c = readInts()
    if b-1 not in graph[a-1] or graph[a-1][b-1] > c:
        graph[a-1][b-1] = graph[b-1][a-1] = c

weights = []
pq = [(0, 0)]
visited = [False] * (n + 1)
while len(pq) != 0:
    c, x = heapq.heappop(pq)
    if visited[x]:
        continue

    visited[x] = True
    weights.append(c)
    for k, v in graph[x].items():
        if not visited[k]:
            heapq.heappush(pq, (v, k))

tot = 0
big = 0
for w in weights:
    tot += w
    if w > big:
        big = w

print(tot - big)
