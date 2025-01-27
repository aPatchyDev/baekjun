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

# Max distance from leaf node to leaf node

n = readInt()
tree = [dict() for _ in range(n)]
for _ in range(n - 1):
    a, b, c = readInts()
    tree[a - 1][b - 1] = c
    tree[b - 1][a - 1] = c

leaves = set()
stk = [0]
visited = [False] * (n + 1)
while len(stk) != 0:
    p = stk.pop()
    if visited[p]:
        continue

    visited[p] = True
    if len(tree[p]) == 1:
        leaves.add(p)
    
    stk.extend(tree[p].keys())

res = 0
for l in leaves:
    visited = [False] * n
    visited[l] = True
    stk = [(l, 0)]
    while len(stk) != 0:
        p, d = stk.pop()

        for q, v in tree[p].items():
            if not visited[q]:
                visited[q] = True
                res = max(res, d + v)
                stk.append((q, d + v))

print(res)