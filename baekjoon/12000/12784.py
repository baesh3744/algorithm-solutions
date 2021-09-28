import sys


INF: int = sys.maxsize

input = sys.stdin.readline

visited: list[bool]
graph: list[list[tuple[int, int]]]


def dfs(node: int) -> int:
    visited[node] = True

    if len(graph[node]) == 1 and node != 1:
        return INF

    dynamite: int = 0
    for child, dyn in graph[node]:
        if not visited[child]:
            dynamite += min(dyn, dfs(child))
    return dynamite


def main() -> None:
    global visited, graph
    t = int(input())
    for _ in range(t):
        n, m = map(int, input().split())

        graph = [[] for _ in range(n + 1)]
        for _ in range(m):
            node1, node2, dynamite = map(int, input().split())
            graph[node1].append((node2, dynamite))
            graph[node2].append((node1, dynamite))

        visited = [False for _ in range(n + 1)]
        visited[1] = True
        print(dfs(1))


if __name__ == "__main__":
    main()
