import sys


MAX = sys.maxsize

input = sys.stdin.readline


def floyd_warshall() -> list[list[int]]:
    dists: list[list[int]] = [[MAX for _ in range(n + 1)] for _ in range(n + 1)]

    for node in range(1, n + 1):
        dists[node][node] = 0

    for s, e, l in paths:
        dists[s][e] = dists[e][s] = min(dists[s][e], l)

    for through in range(1, n + 1):
        for start in range(1, n + 1):
            for end in range(1, n + 1):
                dists[start][end] = min(
                    dists[start][end], dists[start][through] + dists[through][end]
                )

    return dists


def get_maxtime(start: int) -> float:
    maxtime: float = 0.0
    for s, e, l in paths:
        time: float = (dists[start][s] + dists[start][e] + l) / 2
        maxtime = max(maxtime, time)
    return maxtime


if __name__ == "__main__":
    n, m = map(int, input().split())
    paths = [list(map(int, input().split())) for _ in range(m)]

    dists = floyd_warshall()

    ans: float = float("inf")
    for node in range(1, n + 1):
        ans = min(ans, get_maxtime(node))
    print(ans)
