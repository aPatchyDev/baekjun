#!/usr/bin/python3

import heapq

def prim(graph):
    visited = [False] * len(graph)
    parents = [0] * len(graph)
    pq = [(0, 0, 0)]
    weight = 0
    while len(pq) != 0:
        d, x, p = heapq.heappop(pq)
        if visited[x]:
            continue

        visited[x] = True
        # Mark as visited only after extracting from PQ
        weight += d
        parents[x] = p
        for k, v in graph[x].items():
            if not visited[x]:
                heapq.heappush(pq, (v, k, x))

    return weight, parents
