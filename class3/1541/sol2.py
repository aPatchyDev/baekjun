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

# 최솟값은 - 부호 사이만 묶어주면 된다
parts = read().split("-")
groups = [sum(map(int, part.split("+"))) for part in parts]
print(groups[0] - sum(groups[1:]))
