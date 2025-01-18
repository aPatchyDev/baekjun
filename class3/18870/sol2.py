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

pruned = list(set(nums))
pruned.sort()

rank = dict()
for i, v in enumerate(pruned):
    rank[v] = i

print(" ".join(map(str, (rank[v] for v in nums))))

# Creation of pruned: O(n)
# pruned.sort(): Omega(nlogn)
# Creation of rank: Omega(n)
# Mapping to rank: O(n)
# If data has lots of duplicates, runtime becomes much shorter
