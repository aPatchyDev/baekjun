#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

a, b = readInts()

import math
g = math.gcd(a, b)
l = a * b // g

print(g, l, sep="\n")
