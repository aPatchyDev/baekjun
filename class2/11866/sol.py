#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n, k = readInts()
seq = [i for i in range(1, n + 1)]
out = [0] * n

p = 0
for i, l in zip(range(n), range(n, 0, -1)):
    p = (p + k - 1) % l
    out[i] = seq.pop(p)

print(f"<{str(out)[1:-1]}>")

# Cannot calculate pop index with k, l since wrap-around length changes each iteration
