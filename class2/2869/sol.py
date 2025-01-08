#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

a, b, v = readInts()

import math
print(math.ceil((v - a) / (a - b)) + 1)
