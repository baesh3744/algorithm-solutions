import sys
from copy import deepcopy


input = sys.stdin.readline

visited_all: int
cache: list[list[int]]
distances: list[list[int]]
path_list: list[list[int]]


def floyd_warshall(n: int, distances_input: list[list[int]]) -> None:
    global distances, path_list
    distances = deepcopy(distances_input)
    path_list = [[(1 << ridx) | (1 << cidx) for cidx in range(n)] for ridx in range(n)]
    for through in range(n):
        for start in range(n):
            for end in range(n):
                distance: int = distances[start][through] + distances[through][end]
                if distance < distances[start][end]:
                    distances[start][end] = distance
                    path_list[start][end] = (
                        1 << through
                        | path_list[start][through]
                        | path_list[through][end]
                    )


def dp(n: int, planet: int, visited: int) -> int:
    if visited == visited_all:
        return 0
    if cache[planet][visited] != -1:
        return cache[planet][visited]

    ret: int = sys.maxsize
    for next_planet in range(n):
        if ((visited >> next_planet) & 1) == 0:
            next_visited: int = visited | path_list[planet][next_planet]
            ret = min(
                ret,
                distances[planet][next_planet] + dp(n, next_planet, next_visited),
            )
    cache[planet][visited] = ret
    return cache[planet][visited]


def main() -> None:
    global visited_all, cache
    n, k = map(int, input().split())
    distances_input = [list(map(int, input().split())) for _ in range(n)]

    visited_all = (1 << n) - 1
    cache = [[-1 for _ in range(1 << n)] for _ in range(n)]
    floyd_warshall(n, distances_input)
    print(dp(n, k, 1 << k))


if __name__ == "__main__":
    main()
