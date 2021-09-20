import sys
from typing import List


MAX: int = sys.maxsize


def floyd_warshall(n: int, fares: List[List[int]]) -> List[List[int]]:
    distance_list: List[List[int]] = [[MAX for _ in range(n)] for _ in range(n)]

    for node in range(n):
        distance_list[node][node] = 0

    for start, end, distance in fares:
        distance_list[start - 1][end - 1] = distance
        distance_list[end - 1][start - 1] = distance

    for through in range(n):
        for start in range(n):
            for end in range(n):
                distance_list[start][end] = min(
                    distance_list[start][end],
                    distance_list[start][through] + distance_list[through][end],
                )

    return distance_list


def solution(n: int, s: int, a: int, b: int, fares: List[List[int]]) -> int:
    distance_list = floyd_warshall(n, fares)
    return min(
        distance_list[s - 1][through]
        + distance_list[through][a - 1]
        + distance_list[through][b - 1]
        for through in range(n)
    )


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
