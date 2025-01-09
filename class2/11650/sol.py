#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())


pos = [tuple(readInts()) for _ in range(readInt())]
# pos.sort(key=lambda x: (x[0], x[1])) already default behavior
pos.sort()

print("\n".join(f"{x[0]} {x[1]}" for x in pos))
