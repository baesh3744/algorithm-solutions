import sys
from heapq import heappop, heappush


MAX = sys.maxsize
input = sys.stdin.readline


def dijkstra(v: int, start: int, edges: list[list[tuple[int, int]]]) -> list[int]:
    weights: list[int] = [MAX for _ in range(v + 1)]
    heap: list[tuple[int, int]] = []

    weights[start] = 0
    heappush(heap, (0, start))

    while heap:
        weight, vertex = heappop(heap)

        if weights[vertex] < weight:
            continue

        for adj_weight, adj_vertex in edges[vertex]:
            next_weight: int = adj_weight + weight

            if next_weight < weights[adj_vertex]:
                weights[adj_vertex] = next_weight
                heappush(heap, (next_weight, adj_vertex))

    return weights


def main() -> None:
    v, e = map(int, input().split())
    k = int(input())

    edges: list[list[tuple[int, int]]] = [[] for _ in range(v + 1)]
    for _ in range(e):
        _u, _v, _w = map(int, input().split())
        edges[_u].append((_w, _v))

    weights = dijkstra(v, k, edges)
    for weight in weights[1:]:
        print(weight if weight != MAX else "INF")


if __name__ == "__main__":
    main()
