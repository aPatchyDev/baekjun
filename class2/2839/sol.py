#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n = readInt()
if n == 4 or n == 7:
    print(-1)
else:
    q, r = divmod(n, 5)

    # r = 0: 5 x q              ->               q
    # r = 1: 5 x (q - 1) + 6    -> (q - 1) + 2 = q + 1
    # r = 2: 5 x (q - 2) + 12   -> (q - 2) + 4 = q + 2
    # r = 3: 5 x q       + 3    ->             = q + 1
    # r = 4: 5 x (q - 1) + 9    -> (q - 1) + 3 = q + 2
    extra = (0, 1, 2, 1, 2)

    print(q + extra[r])
