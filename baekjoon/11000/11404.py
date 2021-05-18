import sys
from typing import Final


INF: Final[int] = sys.maxsize


def floyd_warshall(n: int, links: list[list[int]]) -> list[list[int]]:
    distances: list[list[int]] = [[INF for _ in range(n)] for _ in range(n)]

    for node in range(n):
        distances[node][node] = 0
    for start, end, distance in links:
        ridx: int = start - 1
        cidx: int = end - 1
        distances[ridx][cidx] = min(distances[ridx][cidx], distance)

    for through in range(n):
        for start in range(n):
            for end in range(n):
                distances[start][end] = min(distances[start][end],
                                            distances[start][through] + distances[through][end])

    for start in range(n):
        for end in range(n):
            if distances[start][end] == INF:
                distances[start][end] = 0

    return distances


def main() -> None:
    n = int(input())
    m = int(input())
    links: list[list[int]] = []
    for _ in range(m):
        a, b, c = map(int, sys.stdin.readline().split())
        links.append([a, b, c])

    for row in floyd_warshall(n, links):
        print(' '.join(map(str, row)))


if __name__ == "__main__":
    main()
