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

n, m, b = readInts()
heights = [nums for _ in range(n) for nums in readInts()]
layer = n * m

short = min(heights)
tall = max(heights)

cost = layer * 512
h = 0
for l in range(short, tall + 1):
    # up, down은 sum(generator) 쓸 때 시간초과 남
    up = 0
    down = 0
    for x in heights:
        if x < l:
            down += l - x
        elif l < x:
            up += x - l

    if down > b + up:
        break

    t = 2 * up + down
    if t <= cost:
        h = l
        cost = t

print(cost, h)
