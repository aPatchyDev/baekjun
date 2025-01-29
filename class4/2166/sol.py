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

# 신발끈 공식

n = readInt()
coords = [list(readInts()) for _ in range(n)]
coords.append(coords[0])

a = 0
b = 0
for i in range(n):
    a += coords[i][0] * coords[i+1][1]
    b += coords[i][1] * coords[i+1][0]

print(f"{abs(a - b) / 2:.1f}")