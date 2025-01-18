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

# Hint: 2 pointer

n = readInt()
fruits = list(readInts())

res = cnt = 0
i = j = k = 0
kind = []
while k < n:
    cnt += 1
    if fruits[k] not in kind:
        kind.append(fruits[k])

    if len(kind) == 3:
        kind = [fruits[j], fruits[k]]
        i = j
        cnt = k - j + 1

    if fruits[k] != fruits[k - 1]:
        j = k

    res = max(res, cnt)
    k += 1

print(res)
