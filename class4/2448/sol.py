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

# n = 3 * 2^k <= 3072
# 가장 긴 밑변의 길이 (빈칸 포함) = 2 * n - 1
# 전체 높이 = n
# 직전 단계의 각 삼각형마다 밑변의 왼쪽은 왼쪽에 삼각형이 없으면,
# 밑변의 오른쪽은 오른쪽에 삼각형이 없으면 새로운 작은 삼각형 생성

n = readInt()
repeat = n // 2
for k in range(11):
    if repeat == (1 << k):
        break

size = 2 * n - 1
lines = [[' '] * size for _ in range(3)]
lines[0][0] = '*'
lines[1][0] = lines[1][2] = '*'
lines[2][:5] = ['*'] * 5
for lead, line in zip(range(n-1, -1, -1), lines):
    print(' ' * lead + ''.join(line[:size-lead]))

# 2nd~ iteration
for lead, base in zip(range(n-4, -1, -3), range(7, 6 * repeat, 6)):
    for i in range(6, base, 6):
        if lines[2][i-2:i+1:2] in [[' ', '*'], ['*', ' ']]:
            lines[0][i] = '*'
            lines[1][i] = lines[1][i+2] = '*'
        else:
            lines[0][i] = ' '
            lines[1][i] = lines[1][i+2] = ' '
    
    for i in range(6, base, 6):
        ch = lines[0][i]
        for j in range(i, i + 5):
            lines[2][j] = ch
    
    print(' ' * lead + ''.join(lines[0][:-lead]))
    print(' ' * (lead - 1) + ''.join(lines[1][:1-lead]))
    print(' ' * (lead - 2) + ''.join(lines[2][:size-lead+2]))