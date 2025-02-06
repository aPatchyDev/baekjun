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
a = list(readInts())
m = readInt()
b = list(readInts())

counta = [0] * 102
countb = [0] * 102

for k in a:
    counta[k] += 1
for k in b:
    countb[k] += 1

for i in range(101):
    countb[i] = min(counta[i], countb[i])

res = []
i = j = 0
k = 100
while  i < n and j < m and k >= 0:
    if countb[k] == 0:
        k -= 1
        continue

    finda = -1
    for x in range(i, n):
        if a[x] == k:
            finda = x
            break

    if finda == -1:
        k -= 1
        continue

    findb = -1
    for x in range(j, m):
        if b[x] == k:
            findb = x
            break

    if findb == -1:
        k -= 1
        continue

    i = finda + 1
    j = findb + 1
    countb[k] -= 1
    res.append(k)

print(len(res))
print(*res)
