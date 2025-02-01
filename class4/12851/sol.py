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

from collections import deque

n, k = readInts()

que = deque()
steps = [100_000] * 200_001

que.append((n, 0))
steps[n] = 0
cnt = 0
while len(que) != 0:
    x, c = que.popleft()
    if x == k:
        cnt += 1
        continue

    if not 0 <= x <= 100_000:
        continue

    for nxt in [x - 1, x + 1, x << 1]:
        if k < x < nxt:
            break

        if steps[nxt] >= c + 1:
            steps[nxt] = c + 1
            que.append((nxt, c + 1))

print(steps[k])
print(cnt)

# 원래 BFS는 방문한 노드를 재방문하지 않지만 여기에서는 경우의 수를 세기 위해 최단거리라면 재방문을 허용한다.
# 노드간 이동시간이 양수이므로 루프가 발생하지 않는다
