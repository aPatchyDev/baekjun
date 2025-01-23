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

n = readInt()
tree = {i: [] for i in range(n)}
for _ in range(n - 1):
    a, b = readInts()
    tree[a - 1].append(b - 1)
    tree[b - 1].append(a - 1)

parent = [0] * (n + 1)
visit = [True] + [False] * n
stk = [0]
while len(stk) != 0:
    p = stk.pop()
    for v in tree[p]:
        if not visit[v]:
            parent[v] = p + 1
            visit[v] = True
            stk.append(v)

for i in range(1, n):
    print(parent[i])
