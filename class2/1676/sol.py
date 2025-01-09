#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

# 5 ** 2 = 25
# 5 ** 3 = 125
# 5 ** 4 = 625 > max(n)

n = readInt()
print(n // 5 + n // 25 + n // 125)
