#!/usr/bin/python3

import heapq
inf = 2 << 62

def dijkstra(graph, start):
    dists = [inf] * len(graph)
    pq = [(0, start)]
    dists[start] = 0
    while len(pq) != 0:
        d, x = heapq.heappop(pq)
        if dists[x] < d:
            # Don't use <= when visiting nodes before adding to PQ
            continue

        for k, v in graph[x].items():
            if dists[k] > d + v:
                dists[k] = d + v
                heapq.heappush(pq, (d + v, k))

    return dists