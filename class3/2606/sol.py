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
graph = [set() for _ in range(n + 1)]
for _ in range(readInt()):
    a, b = readInts()
    graph[a].add(b)
    graph[b].add(a)

stk = [1]
visit = set()
while len(stk) > 0:
    k = stk.pop()
    if k in visit:
        continue

    visit.add(k)
    for x in graph[k]:
        stk.append(x)

print(len(visit) - 1)
