#!/usr/bin/python3

inf = 2 << 62

def floydwarshall(graph):
    n = len(graph)
    dists = [[inf] * n for _ in range(n)]
    for i in range(n):
        dists[i] = 0
        for k, v in graph[i].items():
            dists[i][k] = v

    # k must be the outer-most loop
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dists[i][j] > dists[i][k] + dists[k][j]:
                    dists[i][j] = dists[i][k] + dists[k][j]

    return dists