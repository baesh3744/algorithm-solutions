import sys
from collections import deque


Graph = list[list[tuple[int, int]]]

input = sys.stdin.readline


def get_farthest(n: int, start: int, graph: Graph) -> list[int]:
    que: deque[int] = deque()
    distances = [-1] * (n+1)

    que.append(start)
    distances[start] = 0

    while que:
        cur_node = que.popleft()
        for next_node, dist in graph[cur_node]:
            if distances[next_node] == -1:
                que.append(next_node)
                distances[next_node] = distances[cur_node] + dist
    return distances


def main() -> None:
    n = int(input())

    graph: Graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        from_, to_, length = map(int, input().split())
        graph[from_].append((to_, length))
        graph[to_].append((from_, length))

    distances_one = get_farthest(n, 1, graph)

    start = distances_one.index(max(distances_one))
    distances_start = get_farthest(n, start, graph)

    end = distances_start.index(max(distances_start))
    distances_end = get_farthest(n, end, graph)

    for node in range(1, n+1):
        print(max(distances_start[node], distances_end[node]))


if __name__ == "__main__":
    main()
