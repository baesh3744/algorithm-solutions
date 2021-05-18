import heapq
import sys
from typing import Final


INF: Final[int] = sys.maxsize


def dijkstra(n: int, start: int, graph: dict[int, dict[int, int]]) -> list[int]:
    distances: list[int] = [INF for _ in range(n + 1)]
    que: list[tuple[int, int]] = []

    distances[start] = 0
    heapq.heappush(que, (0, start))

    while que:
        cur_distance, cur_city = heapq.heappop(que)

        if distances[cur_city] < cur_distance:
            continue

        for adj_city, adj_distance in graph[cur_city].items():
            distance: int = cur_distance + adj_distance
            if distance < distances[adj_city]:
                distances[adj_city] = distance
                heapq.heappush(que, (distance, adj_city))

    return distances


def get_destinations(n: int,
                     start: int,
                     through1: int,
                     through2: int,
                     dest_candidates: list[int],
                     graph: dict[int, dict[int, int]]) -> list[int]:
    destinations: list[int] = []

    dijkstra_start = dijkstra(n, start, graph)
    dijkstra_through1 = dijkstra(n, through1, graph)
    dijkstra_through2 = dijkstra(n, through2, graph)

    for candidate in dest_candidates:
        distance_through1: int = dijkstra_start[through1] + \
            graph[through1][through2] + dijkstra_through2[candidate]
        distance_through2: int = dijkstra_start[through2] + \
            graph[through2][through1] + dijkstra_through1[candidate]
        if dijkstra_start[candidate] == distance_through1 or dijkstra_start[candidate] == distance_through2:
            destinations.append(candidate)

    return destinations


def main() -> None:
    test_case = int(input())
    for _ in range(test_case):
        cnt_city, cnt_road, cnt_destination = map(
            int, sys.stdin.readline().split())
        start, through1, through2 = map(int, sys.stdin.readline().split())
        graph: dict[int, dict[int, int]] = {city: {}
                                            for city in range(1, cnt_city + 1)}
        for _ in range(cnt_road):
            city1, city2, distance = map(int, sys.stdin.readline().split())
            graph[city1][city2] = distance
            graph[city2][city1] = distance
        dest_candidates: list[int] = []
        for _ in range(cnt_destination):
            candidate = int(sys.stdin.readline())
            dest_candidates.append(candidate)

        destinations = get_destinations(
            cnt_city, start, through1, through2, dest_candidates, graph)
        print(' '.join(map(str, sorted(destinations))))


if __name__ == "__main__":
    main()
