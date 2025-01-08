#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

out = []

while True:
    a, b, c = readInts()
    if a == b == c == 0:
        break

    a = a * a
    b = b * b
    c = c * c
    d = max(a, b, c) * 2
    if a + b + c == d:
        out.append("right")
    else:
        out.append("wrong")

print('\n'.join(out))
