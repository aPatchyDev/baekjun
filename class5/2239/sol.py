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

# 입력 제한으로 제공된 12095번 소스 해석
# a[x][y] = 스도쿠 퍼즐판
# c[x][i] = x행에 i가 사용되었는지 기록
# c2[y][i] = y열에 i가 사용되었는지 기록
# c3[k][i] = k번째 네모에 i가 사용되었는지 기록
# 빈 칸에 대해 사용되지 않은 숫자를 하나씩 대입하며 재귀로 backtracking
# = 해답이 있는 스도쿠 퍼즐로 입력을 제한한다

game = [list(map(int, list(read()))) for _ in range(9)]

row = [[False] * 11 for _ in range(9)]
col = [[False] * 11 for _ in range(9)]
sqr = [[[False] * 11 for _ in range(3)] for _ in range(3)]

for x in range(9):
    for y in range(9):
        k = game[x][y]
        row[x][k] = col[y][k] = sqr[x // 3][y // 3][k] = True

def nxtpos(x, y):
    j = y
    for i in range(x, 9):
        while j < 9:
            if game[i][j] == 0:
                return i, j
            j += 1
        j = 0

    return 9, 9

def sol(x, y):
    # Can the game be solved by updating game[x][y] ?
    global row, col, sqr, game

    if x == 9:
        for row in game:
            print(''.join(map(str, row)))
        exit()

    for k in range(1, 10):
        if row[x][k] or col[y][k] or sqr[x // 3][y // 3][k]:
            continue

        row[x][k] = col[y][k] = sqr[x // 3][y // 3][k] = True
        game[x][y] = k
        sol(*nxtpos(x, y))
        game[x][y] = 0
        row[x][k] = col[y][k] = sqr[x // 3][y // 3][k] = False


sol(*nxtpos(0, 0))
