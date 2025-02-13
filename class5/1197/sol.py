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

import heapq

v, e = readInts()
graph = [dict() for _ in range(v)]
for _ in range(e):
    a, b, c = readInts()
    if b-1 not in graph[a-1] or graph[a-1][b-1] > c:
        graph[a-1][b-1] = c
        graph[b-1][a-1] = c

res = 0
visited = [False] * (v+1)
pq = [(0, 0)]
while len(pq) != 0:
    c, v = heapq.heappop(pq)
    if visited[v]:
        continue

    visited[v] = True
    res += c
    for nxt, c in graph[v].items():
        if not visited[nxt]:
            heapq.heappush(pq, (c, nxt))

print(res)
