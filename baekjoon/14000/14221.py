import heapq
import sys
from typing import Dict, List, Tuple


def get_distances(graph: Dict[int, Dict[int, int]], convenience: int) -> Dict[int, int]:
    distances: Dict[int, int] = {node: sys.maxsize for node in graph}
    que: List[Tuple[int, int]] = []

    distances[convenience] = 0
    heapq.heappush(que, (0, convenience))

    while que:
        cur_distance, cur_node = heapq.heappop(que)

        if distances[cur_node] < cur_distance:
            continue

        for adj_node, adj_distance in graph[cur_node].items():
            distance: int = cur_distance + adj_distance
            if distance < distances[adj_node]:
                distances[adj_node] = distance
                heapq.heappush(que, (distance, adj_node))

    return distances


def get_closest_home(homes: List[int], conveniences: List[int], graph: Dict[int, Dict[int, int]]) -> int:
    min_distance: int = 500000000
    closest_home: int = 0

    for conv in conveniences:
        distances: Dict[int, int] = get_distances(graph, conv)
        for home in homes:
            if ((distances[home] < min_distance)
                    or (distances[home] == min_distance and home < closest_home)):
                min_distance = distances[home]
                closest_home = home

    return closest_home


def main() -> None:
    n, m = map(int, input().split())
    graph: Dict[int, Dict[int, int]] = {node: {} for node in range(1, n + 1)}
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        graph[a][b] = c
        graph[b][a] = c
    _, _ = map(int, input().split())
    homes = list(map(int, input().split()))
    conveniences = list(map(int, input().split()))

    print(get_closest_home(homes, conveniences, graph))


if __name__ == "__main__":
    main()
