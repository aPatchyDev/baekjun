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

# 임의의 정점에서 제일 먼 정점이 지름의 한쪽 끝이다

v = readInt()
graph = [dict() for _ in range(v)]
for _ in range(v):
    s, *info, _ = readInts()
    for i in range(0, len(info), 2):
        e, d = info[i:i+2]
        graph[s-1][e-1] = d

dist = [1 << 30] * v

def dfs(start):
    dist[start] = 0
    stk = [start]
    while len(stk) != 0:
        x = stk.pop()
        for y in graph[x]:
            if dist[y] > dist[x] + graph[x][y]:
                dist[y] = dist[x] + graph[x][y]
                stk.append(y)

    res = -1
    idx = 0
    for i, e in enumerate(dist):
        if e > res:
            res = e
            idx = i

    return idx, res

p, _ = dfs(0)

for i in range(v):
    dist[i] = 1 << 30

_, d = dfs(p)
print(d)
