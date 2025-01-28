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

n = readInt()

lines = ['  *  ', ' * * ', '*****']
k = 3
while n != k:
    lead = ' ' * k
    k <<= 1

    for i, v in enumerate(lines[:]):
        # Generate two copies of the top triangle
        lines.append(v + ' ' + v)
        
        # Pad previous lines
        lines[i] = lead + v + lead
    

print('\n'.join(lines))