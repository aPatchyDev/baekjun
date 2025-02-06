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

# Bellman Ford로 사이클 탐지시 시작노드는 중요하지 않다

for _ in range(readInt()):
    n, m, w = readInts()
    graph = [dict() for _ in range(n)]
    for _ in range(m):
        s, e, t = readInts()
        if e-1 not in graph[s-1] or graph[s-1][e-1] > t:
            graph[s-1][e-1] = t
            graph[e-1][s-1] = t

    for _ in range(w):
        s, e, t = readInts()
        graph[s-1][e-1] = -t

    dist = [1 << 30] * (n + 1)
    dist[0] = 0
    for k in range(n-1):
        for i in range(n):
            for j in graph[i]:
                if dist[j] > dist[i] + graph[i][j]:
                    dist[j] = dist[i] + graph[i][j]

    for i in range(n):
        for j in graph[i]:
            if dist[j] > dist[i] + graph[i][j]:
                print("YES")
                break
        else:
            continue
        break
    else:
        print("NO")
