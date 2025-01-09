#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())


pos = [tuple(readInts())[::-1] for _ in range(readInt())]
pos.sort()

print("\n".join(f"{x[1]} {x[0]}" for x in pos))
