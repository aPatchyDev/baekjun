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

# A -> B 는 경우의 수가 많으나
# B -> A 는 항상 한 가지 연산만 가능하다

a, b = readInts()
cnt = 1
while b > a:
    cnt += 1
    if b & 1 == 0:
        b >>= 1
    elif b % 10 == 1:
        b //= 10
    else:
        break

if a == b:
    print(cnt)
else:
    print(-1)
