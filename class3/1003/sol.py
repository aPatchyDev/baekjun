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

# fib(0): 1, 0
# fib(1): 0, 1
# fib(2): fib(1) + fib(0) = 0, 1 + 1, 0 = 1, 1
# fib(3): fib(2) + fib(1) = 1, 1 + 0, 1 = 1, 2
# fib(4): fib(3) + fib(2) = 1, 2 + 1, 1 = 2, 3
# fib(5): fib(4) + fib(3) = 2, 3 + 1, 2 = 3, 5
# fib(n > 0): fib(n-1), fib(n)

fib = [0, 1]
for i in range(39):
    fib.append(fib[-2] + fib[-1])

fib.append(1) # fib[-1] = 1

for _ in range(readInt()):
    k = readInt()
    print(fib[k - 1], fib[k])
