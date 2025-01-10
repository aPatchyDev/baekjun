#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

for _ in range(readInt()):
    st = []
    for ch in read():
        if ch == "(":
            st.append(ch)
        elif len(st) == 0:
            print("NO")
            break
        else:
            st.pop()
    else:
        print("YES" if len(st) == 0 else "NO")
