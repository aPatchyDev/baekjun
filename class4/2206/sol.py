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

# 시작과 끝에서 BFS로 거리 기록
# 현재칸 이동거리 + 벽 너머의 남은 거리 최소화

from collections import deque

n, m = readInts()
graph = [list(map(int, list(read()))) for _ in range(n)]

start = [[1 << 30] * m for _ in range(n)]
end = [[1 << 30] * m for _ in range(n)]
start[0][0] = end[n-1][m-1] = 1

offsets = [[-1, 0], [1, 0], [0, -1], [0, 1]]

que = deque()
que.append((0,0,2))
while len(que) != 0:
    x, y, d = que.popleft()
    for dx, dy in offsets:
        if not (0 <= x+dx < n and 0 <= y+dy < m):
            continue

        if graph[x+dx][y+dy] == 0 and start[x+dx][y+dy] == 1 << 30:
            start[x+dx][y+dy] = d
            que.append((x+dx, y+dy, d+1))

que.append((n-1,m-1,2))
while len(que) != 0:
    x, y, d = que.popleft()
    for dx, dy in offsets:
        if not (0 <= x+dx < n and 0 <= y+dy < m):
            continue

        if graph[x+dx][y+dy] == 0 and end[x+dx][y+dy] == 1 << 30:
            end[x+dx][y+dy] = d
            que.append((x+dx, y+dy, d+1))

short = start[n-1][m-1]
# Reuse graph matrix as visited matrix
graph[0][0] = True
stk = [(0, 0)]
while len(stk) != 0:
    x, y = stk.pop()
    for dx, dy in offsets:
        nx = x + dx
        ny = y + dy
        if not (0 <= nx < n and 0 <= ny < m):
            continue
        if graph[nx][ny] != True and start[nx][ny] != 1 << 30:
            graph[nx][ny] = True
            stk.append((nx, ny))

        for di, dj in offsets:
            i = nx + di
            j = ny + dj
            if 0 <= i < n and 0 <= j < m:
                short = min(short, start[x][y] + end[i][j] + 1)


if short == 1 << 30:
    print(-1)
else:
    print(short)
