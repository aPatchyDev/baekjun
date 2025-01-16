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

n = readInt()

from collections import deque
cache = dict()
que = deque()
que.append((n, 0))
while len(que) > 0:
    k, cnt = que.popleft()
    if k in cache and cache[k] <= cnt:
        continue

    cache[k] = cnt
    i = 1
    while i * i < k:
        que.append((k - i * i, cnt + 1))
        i += 1

    if i * i == k:
        print(cnt + 1)
        break
