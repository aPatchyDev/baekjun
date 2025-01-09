#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

w = list(set(read() for _ in range(readInt())))
# w.sort(key=lambda x: (len(x), x))
# For some reason, sorting alphabetically then by length is slightly faster
# Perhaps due to not creating tuples each time..?
w.sort()
w.sort(key=lambda x: len(x))
print("\n".join(w))
