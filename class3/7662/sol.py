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

import heapq

for _ in range(readInt()):
    minh = []
    maxh = []
    rm = [True] * 1_000_001
    cnt = 0
    for _ in range(readInt()):
        op, val = read().split()
        if op == "I":
            k = int(val)
            heapq.heappush(minh, (k, cnt))
            heapq.heappush(maxh, (-k, cnt))
            cnt += 1
        elif val == "1":
            while len(maxh) > 0:
                _, c = heapq.heappop(maxh)
                if rm[c]:
                    rm[c] = False
                    break
        else:
            while len(minh) > 0:
                _, c = heapq.heappop(minh)
                if rm[c]:
                    rm[c] = False
                    break

    while len(maxh) > 0:
        big, c = heapq.heappop(maxh)
        if rm[c]:
            break
    else:
        print("EMPTY")
        continue

    while len(minh) > 0:
        small, c = heapq.heappop(minh)
        if rm[c]:
            break
    else:
        print("EMPTY")
        continue

    print(-big, small)

# Bitarray 사용시 시간초과
