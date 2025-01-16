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

# n-1에서 2x1 추가하는 경우 1개
# n-2에서 1x2 추가하는 경우 1개
# n-2에서 2x2 추가하는 경우 1개
# n=1: 1
# n=2: 3
# n=3: 5

n = readInt()
if n == 1:
    print(1)
else:
    a, b = 1, 3
    for _ in range(n - 2):
        # 작은 수만 다루도록 미리 나머지 처리
        a, b = b, (a * 2 + b) % 10007

    print(b)
