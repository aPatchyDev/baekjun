#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

n = readInt()
data = [tuple(readInts()) for _ in range(n)]
pos = [1] * n

for i, e in enumerate(data):
    for x in data:
        if x[0] > e[0] and x[1] > e[1]:
            pos[i] += 1

print(*pos)

# 정의된 비교 연산에 따라 1, 1, 2 와 같은 등수도 가능하므로 brute force하기
