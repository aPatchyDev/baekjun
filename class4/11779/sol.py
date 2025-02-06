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

n = readInt()
m = readInt()
graph = [dict() for _ in range(n + 1)]
for _ in range(m):
    s, e, c = readInts()
    if e not in graph[s] or graph[s][e] > c:
        graph[s][e] = c

start, end = readInts()

prev = [0] * (n + 1)
dist = [1 << 30] * (n + 1)
prev[start] = start
dist[start] = 0

pq = [(0, start)]
while len(pq) != 0:
    d, x = heapq.heappop(pq)
    if dist[x] < d:
        continue

    for y, c in graph[x].items():
        if dist[y] > d + c:
            dist[y] = d + c
            prev[y] = x
            heapq.heappush(pq, (d + c, y))

path = [end]
x = end
while x != start:
    x = prev[x]
    path.append(x)

print(dist[end])
print(len(path))
print(*reversed(path))
