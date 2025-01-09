#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

from collections import deque

out = []
while True:
    line = read()
    if line == ".":
        break

    st = deque()

    for ch in line:
        if ch in "[(":
            st.append(ch)
        elif ch == "]":
            if len(st) == 0 or st.pop() != "[":
                out.append("no")
                break
        elif ch == ")":
            if len(st) == 0 or st.pop() != "(":
                out.append("no")
                break
        elif ch == "." and len(st) != 0:
            out.append("no")
            break
    else:
        out.append("yes")

print("\n".join(out))
