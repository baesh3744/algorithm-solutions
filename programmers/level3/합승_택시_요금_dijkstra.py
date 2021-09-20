import heapq
import sys
from typing import List, Tuple


MAX: int = sys.maxsize


def fares_to_edge_list(n: int, fares: List[List[int]]) -> List[List[Tuple[int, int]]]:
    edge_list: List[List[Tuple[int, int]]] = [[] for _ in range(n + 1)]
    for c, d, f in fares:
        edge_list[c].append((d, f))
        edge_list[d].append((c, f))
    return edge_list


def dijkstra(n: int, edge_list: List[List[Tuple[int, int]]], start: int) -> List[int]:
    distance_list: List[int] = [MAX for _ in range(n + 1)]
    que: List[Tuple[int, int]] = []

    distance_list[start] = 0
    heapq.heappush(que, (distance_list[start], start))

    while que:
        cur_distance, cur_node = heapq.heappop(que)

        if distance_list[cur_node] < cur_distance:
            continue

        for adj_node, adj_distance in edge_list[cur_node]:
            distance: int = cur_distance + adj_distance
            if distance < distance_list[adj_node]:
                distance_list[adj_node] = distance
                heapq.heappush(que, (distance, adj_node))

    return distance_list


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    edge_list = fares_to_edge_list(n, fares)

    min_cost: int = MAX
    distance_list_from_start = dijkstra(n, edge_list, s)
    for split_node, cost in enumerate(distance_list_from_start):
        distance_list_from_split_node = dijkstra(n, edge_list, split_node)
        min_cost = min(
            min_cost,
            cost + distance_list_from_split_node[a] + distance_list_from_split_node[b],
        )
    return min_cost


# 82
print(
    solution(
        6,
        4,
        6,
        2,
        [
            [4, 1, 10],
            [3, 5, 24],
            [5, 6, 2],
            [3, 1, 41],
            [5, 1, 24],
            [4, 6, 50],
            [2, 4, 66],
            [2, 3, 22],
            [1, 6, 25],
        ],
    )
)
# 14
print(solution(7, 3, 4, 1, [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]))
# 18
print(
    solution(
        6,
        4,
        5,
        6,
        [
            [2, 6, 6],
            [6, 3, 7],
            [4, 6, 7],
            [6, 5, 11],
            [2, 5, 12],
            [5, 3, 20],
            [2, 4, 8],
            [4, 3, 9],
        ],
    )
)
