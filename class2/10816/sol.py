#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

read()
kv = dict()

for e in readInts():
    if e in kv:
        kv[e] += 1
    else:
        kv[e] = 1

read()
for e in readInts():
    print(kv[e] if e in kv else 0, end=" ")

print()
