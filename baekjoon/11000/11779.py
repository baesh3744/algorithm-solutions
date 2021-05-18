import heapq
import sys
from typing import Final


INF: Final[int] = sys.maxsize


def get_path(end: int, previous: list[int]) -> list[int]:
    path: list[int] = []
    node: int = end
    while node != -1:
        path.append(node)
        node = previous[node]
    return list(reversed(path))


def dijkstra(n: int, start: int, end: int, buses: dict[int, dict[int, int]]) -> tuple[list[int], list[int]]:
    distances: list[int] = [INF for _ in range(n + 1)]
    previous: list[int] = [-1 for _ in range(n + 1)]
    que: list[tuple[int, int]] = []

    distances[start] = 0
    heapq.heappush(que, (distances[start], start))

    while que:
        cur_distance, cur_node = heapq.heappop(que)

        if distances[cur_node] < cur_distance:
            continue

        for adj_node, adj_distance in buses[cur_node].items():
            distance: int = cur_distance + adj_distance

            if distance < distances[adj_node]:
                distances[adj_node] = distance
                previous[adj_node] = cur_node
                heapq.heappush(que, (distance, adj_node))

    return distances, previous


def main() -> None:
    n = int(input())
    m = int(input())
    buses: dict[int, dict[int, int]] = {city: {} for city in range(1, n + 1)}
    for _ in range(m):
        start, end, cost = map(int, sys.stdin.readline().split())
        if end in buses[start]:
            buses[start][end] = min(buses[start][end], cost)
        else:
            buses[start][end] = cost
    start, end = map(int, input().split())

    distances, previous = dijkstra(n, start, end, buses)
    path: list[int] = get_path(end, previous)

    print(distances[end])
    print(len(path))
    print(' '.join(map(str, path)))


if __name__ == "__main__":
    main()
