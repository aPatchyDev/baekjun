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

read()

res = 1
curr_cnt = cnt = 0
curr_fruit = prev_fruit = 0
for fruit in readInts():
    if fruit == curr_fruit:
        cnt += 1
        curr_cnt += 1
    elif fruit == prev_fruit:
        curr_fruit, prev_fruit = fruit, curr_fruit
        cnt += 1
        curr_cnt = 1
    else:
        res = max(res, cnt)
        curr_fruit, prev_fruit = fruit, curr_fruit
        cnt = curr_cnt + 1
        curr_cnt = 1

print(max(res, cnt))
