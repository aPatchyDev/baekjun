#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

# d(2~7) = 1    -> 6
# d(8~19) = 2   -> 12
# d(20~37) = 3  -> 18
# ============================
# a[i] = 거리 i(시작 제외)인 첫 수
# ============================
# a[i] = a[i-1] + 6(i-1)
# ...
# a[2] = a[1]  + 6(1)
# a[1] = 2
# ============================
# a[i] = 2 + 3 * i * (i-1)
# ============================
# a^-1[k] = sqrt(x/3 - 5/12) + 1/2

import math
n = readInt()
if n == 1:
    print(1)
else:
    a = math.sqrt( (4 * n - 5) / 12 ) + 1.5
    print(math.floor(a))
