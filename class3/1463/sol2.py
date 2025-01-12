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

# BFS solution is faster than DP solution

from collections import deque

n = readInt()
visited = set()
que = deque()
que.append((n, 0))

while True:
    k, cnt = que.popleft()
    if k in visited:
        continue

    if k == 1:
        print(cnt)
        break

    visited.add(k)

    if k % 3 == 0:
        que.append((k // 3, cnt + 1))

    if k % 2 == 0:
        que.append((k // 2, cnt + 1))

    que.append((k - 1, cnt + 1))
