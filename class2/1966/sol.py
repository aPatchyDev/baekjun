#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

from collections import deque

for _ in range(readInt()):
    n, t = readInts()
    prio = list(readInts())
    q = deque((i, prio[i]) for i in range(n))

    prio.sort()
    while len(q) > 0:
        j = q.popleft()
        if prio[-1] != j[1]:
            q.append(j)
        elif j[0] == t:
            print(n - len(q))
            break
        else:
            prio.pop()
