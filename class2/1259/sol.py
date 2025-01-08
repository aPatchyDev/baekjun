#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

out = []
while True:
    txt = read()
    if txt == "0":
        break

    k = len(txt) // 2
    if txt[:k] == txt[:-k-1:-1]:
        out.append("yes")
    else:
        out.append("no")

print("\n".join(out))
