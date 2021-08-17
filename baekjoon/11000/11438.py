import sys
from typing import List


LOG: int = 20

input = sys.stdin.readline

n: int
depth_list: List[int]
parent_list: List[List[int]]
graph: List[List[int]]


def calculate_depth(node: int, depth: int) -> None:
    depth_list[node] = depth
    for child in graph[node]:
        if depth_list[child] != -1:
            continue
        parent_list[child][0] = node
        calculate_depth(child, depth + 1)


def set_parent() -> None:
    calculate_depth(1, 0)
    for i in range(1, LOG):
        for node in range(1, n + 1):
            parent_list[node][i] = parent_list[parent_list[node][i - 1]][i - 1]


def lca(u: int, v: int) -> int:
    if depth_list[u] > depth_list[v]:
        u, v = v, u
    for i in range(LOG - 1, -1, -1):
        if depth_list[v] - depth_list[u] >= (1 << i):
            v = parent_list[v][i]
    if u == v:
        return u
    for i in range(LOG - 1, -1, -1):
        if parent_list[u][i] != parent_list[v][i]:
            u = parent_list[u][i]
            v = parent_list[v][i]
    return parent_list[u][0]


def main() -> None:
    global n, depth_list, parent_list, graph
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    depth_list = [-1 for _ in range(n + 1)]
    parent_list = [[-1 for _ in range(LOG)] for _ in range(n + 1)]
    set_parent()

    m = int(input())
    for _ in range(m):
        u, v = map(int, input().split())
        print(lca(u, v))


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
