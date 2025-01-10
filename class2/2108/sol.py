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
e = [readInt() for _ in range(n)]

import statistics

print(round(statistics.mean(e)))
print(statistics.median(e))
mode = statistics.multimode(e)
mode.sort()
print(mode[0] if len(mode) == 1 else mode[1])
print(max(e) - min(e))
