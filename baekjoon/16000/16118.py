import heapq
import sys
from typing import List, Tuple


PathList = List[List[Tuple[int, int]]]

MAX: int = sys.maxsize

input = sys.stdin.readline


def dijkstra(path_list: PathList) -> List[int]:
    distances: List[int] = [MAX for _ in range(len(path_list))]
    heap: List[Tuple[int, int]] = []

    heapq.heappush(heap, (0, 1))
    distances[1] = 0

    while heap:
        dist, tree = heapq.heappop(heap)
        if dist > distances[tree]:
            continue

        for adj_tree, adj_dist in path_list[tree]:
            next_dist: int = dist + adj_dist
            if next_dist < distances[adj_tree]:
                heapq.heappush(heap, (next_dist, adj_tree))
                distances[adj_tree] = next_dist

    return distances


def main() -> None:
    n, m = map(int, input().split())

    fox_path_list: PathList = [[] for _ in range(n + 1)]
    wolf_path_list: PathList = [[] for _ in range(2 * n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        fox_path_list[a].append((b, 2 * d))
        fox_path_list[b].append((a, 2 * d))
        wolf_path_list[a].append((n + b, d))
        wolf_path_list[b].append((n + a, d))
        wolf_path_list[n + a].append((b, 4 * d))
        wolf_path_list[n + b].append((a, 4 * d))

    distances_fox = dijkstra(fox_path_list)
    distances_wolf = dijkstra(wolf_path_list)

    print(
        sum(
            distances_fox[tree] < min(distances_wolf[tree], distances_wolf[tree + n])
            for tree in range(1, n + 1)
        )
    )


if __name__ == "__main__":
    main()


# Reference "flip1945" https://www.acmicpc.net/source/32994738
