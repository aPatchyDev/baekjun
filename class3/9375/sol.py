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

from collections import defaultdict

for _ in range(readInt()):
    wardrobe = defaultdict(lambda: 1)
    for _ in range(readInt()):
        _, kind = read().split()
        wardrobe[kind] += 1

    cnt = 1
    for k in wardrobe.values():
        cnt *= k

    print(cnt - 1)
