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
times = []
for _ in range(n):
    a, b = readInts()
    times.append((b, a))

times.sort()
cnt = 0
end  = 0
for sched in times:
    e, s = sched
    if s >= end:
        cnt += 1
        end = e

print(cnt)
