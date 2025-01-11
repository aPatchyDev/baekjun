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

s = 0
for _ in range(readInt()):
    cmd = read().split()
    match cmd[0]:
        case "add":
            s |= 1 << int(cmd[1])
        case "remove":
            s &= ~(1 << int(cmd[1]))
        case "check":
            print((s >> int(cmd[1])) & 1)
        case "all":
            s = (1 << 21) - 1
        case "empty":
            s = 0
        case "toggle":
            s ^= 1 << int(cmd[1])
