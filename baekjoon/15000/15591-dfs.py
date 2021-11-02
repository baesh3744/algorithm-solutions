import sys
from typing import List, Tuple


MAX_USADO = sys.maxsize

input = sys.stdin.readline

network: List[List[Tuple[int, int]]]


def count(k: int, video: int, min_usado: int) -> int:
    visited[video] = True

    cnt: int = 1
    for adj_video, usado in network[video]:
        next_usado = min(min_usado, usado)
        if not visited[adj_video] and next_usado >= k:
            cnt += count(k, adj_video, next_usado)
    return cnt


def main() -> None:
    global network, visited
    n, q = map(int, input().split())

    network = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        pi, qi, ri = map(int, input().split())
        network[pi].append((qi, ri))
        network[qi].append((pi, ri))

    for _ in range(q):
        visited = [False for _ in range(n + 1)]
        k, v = map(int, input().split())
        print(count(k, v, MAX_USADO) - 1)


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
