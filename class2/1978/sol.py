#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

# 32 ** 2 == 1024
nums = [False, False, True] + [True, False] * 500
for n in range(3, 32, 2):
    if nums[n]:
        for k in range(n * 2, 1000, n):
            nums[k] = False

read()
print(sum(1 for x in readInts() if nums[x]))
