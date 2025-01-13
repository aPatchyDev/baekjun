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

# Shortest Path 변형 (BFS로는 불가능)
# 가중치는 노드에 도달할 때의 점수
# 계단당 노드 2개: 1칸 이동 가능 / 불가능
# graph[0] = {2, 4},    graph[1] = 미사용
# graph[2] = {5, 6},    graph[3] = {6}

n = readInt()
graph = [dict() for _ in range(2 * n + 2)]
for i in range(1, n + 1):
    v = readInt()
    if i == 1:
        graph[0][2] = v # 직전 계단에서 1칸 이동
    else:
        graph[2 * i - 2][2 * i + 1] = v # 직전 계단에서 1칸 이동
        graph[2 * i - 3][2 * i] = v     # 전전 계단에서 2칸 이동
        graph[2 * i - 4][2 * i] = v     # 전전 계단에서 2칸 이동

import heapq
w = [0] * (2 * n + 2)
w[0] = 1        # To start first visit
maxheap = []
heapq.heappush(maxheap, (0, 0))
# MaxHeap를 위해 weight가 양이 아닌 정수로 변형
while len(maxheap) > 0:
    negscore, node = heapq.heappop(maxheap)
    if negscore >= w[node]:
        continue

    w[node] = negscore
    for nxt, point in graph[node].items():
        relax = negscore - point
        if w[nxt] > relax:
            heapq.heappush(maxheap, (relax, nxt))

print(-min(w[-2], w[-1]))
