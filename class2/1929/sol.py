#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

m, n = readInts()
p = [2]
for i in range(3, n + 1, 2):
    flag = True
    for x in p:
        if x ** 2 > i:
            break
        if i % x == 0:
            flag = False
    if flag:
        p.append(i)

import bisect
left = bisect.bisect_left(p, m)
for x in range(left, len(p)):
    print(p[x])
