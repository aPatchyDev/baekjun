#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

m, n = readInts()

if m < 3:
    rng = ((3, n + 1),)
else:
    mid = ((m >> 1) << 1) + 1
    rng = ((3, mid), (mid, n + 1))

left = 0
p = [2]
for r in rng:
    for i in range(*r, 2):
        flag = True
        for x in p:
            if x ** 2 > i:
                break
            if i % x == 0:
                flag = False
        if flag:
            p.append(i)
    if r[1] != n + 1:
        left = len(p)

for x in range(left, len(p)):
    print(p[x])

# Searching for left point with bisect is faster than
# pausing prime generation in the middle
