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

n, r, c = readInts()
if n == 1:
    print((r << 1) | c)
    exit()
elif r == c == 0:
    print(0)
    exit()

lo = 0
hi = 1 << (2 * n)
cnt = 0
while lo + 1 < hi:
    ql = 1 << (n - 1)
    qsize = 1 << (2 * n - 2)

    if r < ql:
        if c < ql:
            hi = lo + qsize
        else:
            hi = lo + 2 * qsize
            lo += qsize
            cnt += qsize
            c -= ql
    else:
        if c < ql:
            hi = lo + 3 * qsize
            lo += 2 * qsize
            cnt += 2 * qsize
            r -= ql
        else:
            lo += 3 * qsize
            cnt += 3 * qsize
            r -= ql
            c -= ql

    n -= 1
    if n == 0:
        print(cnt)
        break
