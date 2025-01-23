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

a, b = readInts()
que = deque()
que.append((a, 1))
visit = set()
while len(que) != 0:
    n, cnt = que.popleft()
    if n == b:
        print(cnt)
        exit()
    elif n < b:
        x = 10 * n + 1
        y = n << 1
        if x not in visit:
            que.append((x, cnt + 1))
            visit.add(x)

        if y not in visit:
            que.append((y, cnt + 1))
            visit.add(y)

print(-1)
