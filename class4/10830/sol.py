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

n, b = readInts()
mat = [list(readInts()) for _ in range(n)]
tmpmat = [[0] * n for _ in range(n)]

res = [[0] * n for _ in range(n)]
tmpres = [[0] * n for _ in range(n)]
for i in range(n):
    res[i][i] = 1

while b > 0:
    if b & 1 == 1:
        for i in range(n):
            for j in range(n):
                acc = 0
                for k in range(n):
                    acc += (res[i][k] * mat[k][j]) % 1000
                
                tmpres[i][j] = acc % 1000
        
        res, tmpres = tmpres, res
    
    b >>= 1
    for i in range(n):
        for j in range(n):
            acc = 0
            for k in range(n):
                acc += (mat[i][k] * mat[k][j]) % 1000
            
            tmpmat[i][j] = acc % 1000
    mat, tmpmat = tmpmat, mat

for row in res:
    print(*row)