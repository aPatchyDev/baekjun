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

# 문제 해석
# k번째 해는 <1 + (k-1) % m, 1 + (k-1) % n>로 표현한다
# <x, y>에서 k를 구해라
# k == x + am == y + bn for some integers a,b >= 0
# k <= (a+1)m == (b+1)n == lcm(m, n) <= mn
# Bruteforce is O(min(m, n))

def sol(bigmod, smallmod, big, small):
    for a in range(0, bigmod * smallmod, bigmod):
        k = a + big - small
        if k >= 0 and k % smallmod == 0:
            return print(k + small)

    print(-1)

for _ in range(readInt()):
    m, n, x, y = readInts()

    if m > n:
        sol(m, n, x, y)
    else:
        sol(n, m, y, x)
