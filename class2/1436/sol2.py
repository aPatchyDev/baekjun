#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

# Generate candidates with d + 3 digits
# Take the sequence [0, 10 ** d)
# Insert 666 anywhere in each number
# Remove duplicates

n = readInt()

if n == 1:
    print(666)
else:
    d = 1 if n <= 19 else \
        2 if n <= 280 else \
        3 if n <= 3700 else \
        4 # if n <= 45991
    seq = set()
    for e in range(10 ** d):
        txt = str(e).zfill(d)
        for i in range(d + 1):
            f = txt[:i]
            b = txt[i:]
            seq.add(int(f"{f}666{b}"))

    print(sorted(seq)[n - 1])
