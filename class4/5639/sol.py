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

nums = list(map(int, sys.stdin.readlines()))
parents = dict()
tree = dict()
prev = nums[0]
parents[prev] = prev
for n in nums[1:]:
    if n > prev:
        while n > parents[prev] and prev != nums[0]:
            prev = parents[prev]
        
        while prev in tree:
            if n < prev:
                if tree[prev][0] is None:
                    break
                prev = tree[prev][0]
            else:
                if tree[prev][1] is None:
                    break
                prev = tree[prev][1]
        
    assert prev is not None
    parents[n] = prev
    if prev not in tree:
        tree[prev] = [None, None]
    
    if n < prev:
        tree[prev][0] = n
    else:
        tree[prev][1] = n

    prev = n

stk = [nums[0]]
while len(stk) != 0:
    k = stk.pop()
    if k not in tree:
        print(k)
        if k == nums[0]:
            break
        if tree[parents[k]][1] in (k, None):
            del tree[parents[k]]
    else:
        stk.append(k)
        for x in reversed(tree[k]):
            if x is not None:
                stk.append(x)