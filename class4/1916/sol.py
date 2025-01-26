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

from collections import defaultdict
import heapq

n = readInt()
m = readInt()
graph = defaultdict(dict)
for _ in range(m):
    s, e, c = readInts()
    if e in graph[s]:
        graph[s][e] = min(graph[s][e], c)
    else:
        graph[s][e] = c

s, e = readInts()

costs = [2 << 62] * (n + 2)
pq = [(0, s)]
while len(pq) != 0:
    prio, node = heapq.heappop(pq)
    if prio >= costs[node]:
        continue

    costs[node] = prio
    for nxt, c in graph[node].items():
        if prio + c < costs[nxt]:
            heapq.heappush(pq, (prio + c, nxt))

print(costs[e])