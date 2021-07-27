import sys
from collections import deque


Graph = list[list[tuple[int, int]]]

input = sys.stdin.readline


def get_farthest(n: int, start: int, graph: Graph) -> tuple[int, int]:
    max_: tuple[int, int] = (0, 0)
    que: deque[int] = deque()
    distances: list[int] = [-1] * (n+1)

    que.append(start)
    distances[start] = 0

    while que:
        cur_node = que.popleft()
        for next_node, dist in graph[cur_node]:
            if distances[next_node] != -1:
                continue
            que.append(next_node)
            distances[next_node] = distances[cur_node] + dist
            if max_[1] < distances[next_node]:
                max_ = next_node, distances[next_node]
    return max_


def main() -> None:
    n = int(input())

    graph: Graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        parent, child, weight = map(int, input().split())
        graph[parent].append((child, weight))
        graph[child].append((parent, weight))

    node, _ = get_farthest(n, 1, graph)
    _, dist = get_farthest(n, node, graph)
    print(dist)


if __name__ == "__main__":
    main()
