import sys
from heapq import heappop, heappush


MAX = sys.maxsize

input = sys.stdin.readline


def dijkstra() -> None:
    heap: list[tuple[int, int]] = []

    heappop(distances[0])
    heappush(distances[0], 0)
    heappush(heap, (0, 0))

    while heap:
        dist, city = heappop(heap)

        for adj_city, adj_dist in paths[city]:
            new_dist: int = dist + adj_dist

            if -distances[adj_city][0] <= new_dist:
                continue

            heappop(distances[adj_city])
            heappush(distances[adj_city], -new_dist)
            heappush(heap, (new_dist, adj_city))


if __name__ == "__main__":
    n, m, k = map(int, input().split())

    paths: list[list[tuple[int, int]]] = [[] for _ in range(n)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        paths[a - 1].append((b - 1, c))

    distances: list[list[int]] = [[-MAX for _ in range(k)] for _ in range(n)]
    dijkstra()
    for dists in distances:
        print(-dists[0] if dists[0] != -MAX else -1)
