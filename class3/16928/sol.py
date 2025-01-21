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

from collections import deque

n, m = readInts()
paths = dict()
for _ in range(n + m):
    s, e = readInts()
    paths[s] = e

que = deque()
que.append(1)

d = [0, 0] + [100] * 100
while len(que) > 0:
    pos = que.popleft()
    cnt = d[pos] + 1
    for i in range(1, 7):
        nxt = pos + i
        if nxt == 100:
            print(cnt)
            exit()

        if nxt in paths:
            nxt = paths[nxt]

        if d[nxt] > cnt:
            d[nxt] = cnt
            que.append(nxt)
