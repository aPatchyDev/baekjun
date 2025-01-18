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

# BFS solution
# V x BFS: V x O(V + E), E <= V^2

n, m = readInts()
graph = {i: set() for i in range(1, n + 1)}
for _ in range(m):
    a, b = readInts()
    graph[a].add(b)
    graph[b].add(a)

from collections import deque

res = 100_000
idx = 0
for i in range(1, n + 1):
    score = 0
    que = deque()
    visit = 0       # bitarray
    que.append((i, 0))
    while len(que) > 0:
        k, d = que.popleft()
        if (visit >> k) & 1 == 1:
            continue

        visit |= 1 << k
        score += d
        for x in graph[k]:
            que.append((x, d + 1))

    if score < res:
        res = score
        idx = i

print(idx)
