#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n = readInt()
sizes = readInts()
t, p = readInts()

import math

print(sum(math.ceil(i / t) for i in sizes))
print(*divmod(n, p))
