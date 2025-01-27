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

n, e = readInts()
graph = [{i: 0} for i in range(n+1)]
for _ in range(e):
    a, b, c = readInts()
    graph[a][b] = c
    graph[b][a] = c

s1, s2 = list(readInts())

def pf(start, p1, p2, p3):
    dists = [2 << 30] * (n+1)
    pq = [(0, start)]
    while len(pq) != 0:
        d, x = heapq.heappop(pq)
        if dists[x] < d:
            continue
    
        dists[x] = d
        for k, v in graph[x].items():
            if dists[k] > d + v:
                dists[k] = d + v
                heapq.heappush(pq, (d + v, k))
    
    return [dists[p1], dists[p2], dists[p3]]

# 방향이 없으니 1->s1 == s1->1
p1, p2, p3 = pf(s1, 1, s2, n)
q1, _, q3 = pf(s2, 1, s1, n)

# 1 -> s1 -> s2 -> n
path1 = p1 + p2 + q3

# 1 -> s2 -> s1 -> n
path2 = q1 + p2 + p3

if path1 >= (2 << 30) and path2 >= (2 << 30):
    print(-1)
else:
    print(min(path1, path2))