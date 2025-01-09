#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n = readInt()
k = 665
while n > 0:
    k += 1
    if "666" in str(k):
        n -= 1

print(k)
