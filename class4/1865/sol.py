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

for _ in range(readInt()):
    n, m, w = readInts()
    dist = [[1 << 30] * n for _ in range(n)]
    for _ in range(m):
        s, e, t = readInts()
        if dist[s-1][e-1] > t:
            dist[s-1][e-1] = t
            dist[e-1][s-1] = t

    for _ in range(w):
        s, e, t = readInts()
        dist[s-1][e-1] = -t

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

            if dist[i][i] < 0:
                print("YES")
                break
        else:
            continue
        break
    else:
        print("NO")
