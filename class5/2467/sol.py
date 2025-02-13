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

n = readInt()
nums = list(readInts())

# 특성값이 최대 10^9 ~= 2^30이므로 합은 2*10^9 이상이어야 한다
tot = 1 << 31
small = big = 0

lo = 0
hi = n - 1
while lo < hi:
    chk = abs(nums[lo] + nums[hi])
    if chk < tot:
        tot = chk
        small = nums[lo]
        big = nums[hi]

    if abs(nums[lo] + nums[hi - 1]) < abs(nums[lo + 1] + nums[hi]):
        hi -= 1
    else:
        lo += 1

print(small, big)
