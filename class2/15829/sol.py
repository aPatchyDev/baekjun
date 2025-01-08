#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

readInt()
txt = read()
a = ord("a") - 1

s = 0
for idx, ch in enumerate(txt):
    s = (s + (ord(ch) - a) * 31 ** idx) % 1234567891

print(s)
