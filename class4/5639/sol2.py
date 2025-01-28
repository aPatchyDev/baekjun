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

# Tree를 복원할 필요가 없다
# 각 노드마다 subtree의 범위 내에서 처음으로 큰 값이 오른쪽 subtree

nums = list(map(int, sys.stdin.readlines()))

def sol(start, end):
    if start == end:
        return

    k = nums[start]
    right = end
    for i in range(start+1, end):
        if nums[i] > k:
            right = i
            break

    sol(start + 1, right) 
    sol(right, end)
    print(k)

sol(0,len(nums))