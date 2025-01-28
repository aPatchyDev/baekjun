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

s = read()
bomb = list(read())
bsize = len(bomb)

res = list(s[:bsize])
for ch in s[bsize:]:
    while res[-bsize:] == bomb:
        del res[-bsize:]

    res.append(ch)

while res[-bsize:] == bomb:
    del res[-bsize:]

if len(res) == 0:
    print('FRULA')
else:
    print(''.join(res))