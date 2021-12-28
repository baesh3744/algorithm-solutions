import sys


MAX = sys.maxsize
input = sys.stdin.readline


def floyd_warshall(rels: list[tuple[int, int]]) -> list[list[int]]:
    dists: list[list[int]] = [[MAX for _ in range(n)] for _ in range(n)]

    for node in range(n):
        dists[node][node] = 0

    for first, second in rels:
        dists[first][second] = 1

    for through in range(n):
        for start in range(n):
            for end in range(n):
                dists[start][end] = min(
                    dists[start][end], dists[start][through] + dists[through][end]
                )

    return dists


def print_answer() -> None:
    for dists_i, rdists_i in zip(dists, rdists):
        cnt: int = 0
        for dist, rdist in zip(dists_i, rdists_i):
            cnt += int(dist == MAX and rdist == MAX)
        print(cnt)


if __name__ == "__main__":
    n = int(input())
    m = int(input())

    rels: list[tuple[int, int]] = []
    rrels: list[tuple[int, int]] = []
    for _ in range(m):
        first, second = map(lambda x: int(x) - 1, input().split())
        rels.append((first, second))
        rrels.append((second, first))

    dists = floyd_warshall(rels)
    rdists = floyd_warshall(rrels)
    print_answer()
