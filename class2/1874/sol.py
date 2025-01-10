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

st = []
ops = []
i = 1
for _ in range(readInt()):
    e = readInt()
    while i <= e:
        st.append(i)
        ops.append("+")
        i += 1

    ops.append("-")
    if st.pop() != e:
        print("NO")
        break
else:
    print("\n".join(ops))
