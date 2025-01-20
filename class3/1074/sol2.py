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

# Cleaner code

n, r, c = readInts()
if r == c == 0:
    print(0)
    exit()

cnt = 0
for i in range(n - 1, 0, -1):
    ql = 1 << i
    qsize = 1 << (2 * i)

    if r < ql:
        if c >= ql:
            cnt += qsize
            c -= ql
    else:
        if c < ql:
            cnt += qsize * 2
            r -= ql
        else:
            cnt += qsize * 3
            r -= ql
            c -= ql


print(cnt + (r << 1) | c)
