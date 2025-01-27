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

from collections import defaultdict

n, m = readInts()
t, *truth = readInts()
truth = set(truth)
grp = defaultdict(list)
parties = []
for i in range(m):
    _, *ppl = readInts()
    parties.append(ppl)

    for p in ppl:
        grp[p].append(i)

canlie = [0] * m
update = set(g for p in truth for g in grp[p])
while len(update) != 0:
    k = update.pop()
    canlie[k] = 1
    before = len(truth)
    truth.update(parties[k])
    if len(truth) != before:
        for p in parties[k]:
            for x in grp[p]:
                update.add(x)

print(m - sum(canlie))