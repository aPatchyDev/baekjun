#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n = readInt()
v = [readInt() for _ in range(n)]
v.sort()

if n == 0:
    print(0)
else:
    import math

    cut = math.floor(0.5 + n * 0.15)
    tot = sum(v[cut:n-cut])
    cnt = n - 2 * cut
    print(math.floor(0.5 + tot / cnt))

# round() rounds to nearest even
# array[0, -0] == [] != array[0, n]
