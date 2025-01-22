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

from collections import deque

for _ in range(readInt()):
    start, end = readInts()
    que = deque()
    que.append(start)
    record = {start: None}

    while len(que) != 0:
        n = que.popleft()
        if n == end:
            break

        dslr = [
            2 * n,
            n - 1,
            10 * (n % 1_000) + n // 1_000,
            n // 10 + 1_000 * (n % 10)
        ]
        for k, op in zip(dslr, "DSLR"):
            x = k % 10_000
            if x not in record:
                record[x] = (n, op)
                que.append(x)

    ops = []
    it = end
    while it != start:
        it, op = record[it]
        ops.append(op)

    print(''.join(reversed(ops)))
