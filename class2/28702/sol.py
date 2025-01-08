#!/usr/bin/python3

import sys
def read():
    return sys.stdin.readline().rstrip()

def readInt():
    return int(sys.stdin.readline())

def readInts():
    return map(int, sys.stdin.readline().split())

# 연속 3개 중 반드시 1개 이상은 숫자를 출력한다

for i in range(3, 0, -1):
    txt = read()
    if txt[0].isnumeric():
        k = int(txt) + i
        out = ""
        if k % 3 == 0:
            out += "Fizz"
        if k % 5 == 0:
            out += "Buzz"
        if out == "":
            out = str(k)

        print(out)
        break
