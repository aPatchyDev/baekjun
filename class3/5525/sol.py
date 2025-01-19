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

# S 안에서 Pk 구간들만 찾기
# Pk 안에 Pn은 k-n+1번 들어간다 (k >= n)

n = readInt()
m = readInt()
s = read()

cnt = 0
lo = s.find("I")
while lo != -1:
    prev = "I"
    hi = lo + 1
    while hi < m:
        if s[hi] == prev:
            k = (hi - lo) // 2
            if k >= n:
                cnt += k - n + 1 if prev == "I" else k - n
            break

        prev = s[hi]
        hi += 1
    else:
        k = (hi - lo) // 2
        if k >= n:
            cnt += k - n + 1 if prev == "I" else k - n

    lo = s.find("I", hi)

print(cnt)

# 다른 풀이를 보니 s[i:i+3]로 slice를 생성해도 실행속도에 타격이 없어 보인다
# PyPy JIT로 최적화되는 듯..?
