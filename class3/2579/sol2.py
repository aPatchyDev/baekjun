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

# DP is much faster than Dijkstra

n = readInt()
w = [readInt() for _ in range(n)]

if n == 1:
    print(w[0])
elif n == 2:
    print(sum(w))
else:
    scores = [0] * n
    scores[0] = w[0]
    scores[1] = sum(w[0:2])
    scores[2] = w[2] + max(w[0:2])
    for i in range(3, n):
        scores[i] = w[i] + max(scores[i-3] + w[i-1], scores[i-2])

    print(scores[-1])
