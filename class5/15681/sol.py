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

n, r, q = readInts()
graph = [[] for _ in range(n+2)]
for _ in range(n-1):
    u, v = readInts()
    graph[u].append(v)
    graph[v].append(u)

childs = [0] * (n+2)
roots = [0] * (n+2)

roots[r] = r
stk = [r]
while len(stk) != 0:
    peek = stk[-1]
    if childs[peek] == 0:
        # First visit - count self, queue child nodes
        childs[peek] = 1
        for x in graph[peek]:
            if x != roots[peek]:
                roots[x] = peek
                stk.append(x)
    else:
        # Second visit - count child nodes
        for x in graph[peek]:
            if x != roots[peek]:
                childs[peek] += childs[x]

        stk.pop()

for _ in range(q):
    print(childs[readInt()])

# Separate loop for each visit is faster due to branch prediction
