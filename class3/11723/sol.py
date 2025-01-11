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

s = [0] * 22
for _ in range(readInt()):
    cmd = read().split()
    match cmd[0]:
        case "add":
            s[int(cmd[1])] = 1
        case "remove":
            s[int(cmd[1])] = 0
        case "check":
            print(s[int(cmd[1])])
        case "all":
            s = [1] * 22
        case "empty":
            s = [0] * 22
        case "toggle":
            s[int(cmd[1])] ^= 1

# This exceeds memory on PyPy3 but passes on Python3
# Switching to boolean does not sufficiently reduce memory usage
# Use set instead of list to reduce memory a little
# Or use bitarray for array of booleans
