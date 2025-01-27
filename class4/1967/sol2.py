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

# Leaf node 중 1개는 가장 먼 노드다

n = readInt()
tree = [dict() for _ in range(n)]
for _ in range(n - 1):
    a, b, c = readInts()
    tree[a - 1][b - 1] = c
    tree[b - 1][a - 1] = c

dists = [0] * (n + 1)
visited = [False] * (n + 1)
stk = [(0, 0)]
while len(stk) != 0:
    p, d = stk.pop()
    if visited[p]:
        continue

    visited[p] = True
    dists[p] = d
    for q, v in tree[p].items():
        if not visited[q]:
            stk.append((q, d + v))

start = 0
dist = 0
for p, d in enumerate(dists):
    if d > dist:
        start = p
        dist = d

visited = [False] * (n + 1)
stk = [(start, 0)]
while len(stk) != 0:
    p, d = stk.pop()
    if visited[p]:
        continue

    visited[p] = True
    dists[p] = d
    for q, v in tree[p].items():
        if not visited[q]:
            stk.append((q, d + v))

print(max(dists))