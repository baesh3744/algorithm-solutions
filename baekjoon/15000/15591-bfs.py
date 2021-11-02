import sys
from collections import deque


input = sys.stdin.readline

network: list[list[tuple[int, int]]]


def count(n: int, k: int, v: int) -> int:
    cnt: int = 0
    que: deque[int] = deque()
    visited: list[bool] = [False for _ in range(n + 1)]

    que.append(v)
    visited[v] = True

    while que:
        video = que.popleft()
        for adj_video, usado in network[video]:
            if not visited[adj_video] and usado >= k:
                cnt += 1
                que.append(adj_video)
                visited[adj_video] = True

    return cnt


def main() -> None:
    global network
    n, q = map(int, input().split())

    network = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        pi, qi, ri = map(int, input().split())
        network[pi].append((qi, ri))
        network[qi].append((pi, ri))

    for _ in range(q):
        k, v = map(int, input().split())
        print(count(n, k, v))


if __name__ == "__main__":
    sys.setrecursionlimit(10000)
    main()
