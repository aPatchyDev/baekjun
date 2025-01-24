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

n = readInt()
tree = dict()
for _ in range(n):
    a, b, c = read().split()
    tree[a] = [b.strip("."), c.strip(".")]

def preord(acc, node):
    if node == "":
        return acc

    return preord(preord(acc + node, tree[node][0]), tree[node][1])

def inord(acc, node):
    if node == "":
        return acc

    return inord(inord(acc, tree[node][0]) + node, tree[node][1])

def postord(acc, node):
    if node == "":
        return acc

    return postord(postord(acc, tree[node][0]), tree[node][1]) + node

print(preord("", "A"))
print(inord("", "A"))
print(postord("", "A"))
