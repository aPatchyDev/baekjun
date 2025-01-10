#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

for _ in range(readInt()):
    n, t = readInts()
    prio = list(readInts())
    q = [(i, prio[i]) for i in range(n)]

    prio.sort()
    k = 0
    while len(q) > 0:
        j = q[k]
        k += 1
        if prio[-1] != j[1]:
            q.append(j)
        elif j[0] == t:
            print(n - len(q) + k)
            break
        else:
            prio.pop()

# Using array is faster than queue (deque)
