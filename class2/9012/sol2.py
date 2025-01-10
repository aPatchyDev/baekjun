#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

for _ in range(readInt()):
    cnt = 0
    for ch in read():
        if ch == "(":
            cnt += 1
        elif cnt == 0:
            print("NO")
            break
        else:
            cnt -= 1
    else:
        print("YES" if cnt == 0 else "NO")
