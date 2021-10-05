import sys


LOG: int = 20

input = sys.stdin.readline

edge_list: list[list[tuple[int, int]]]
distance_list: list[int]
depth_list: list[int]
parent_list: list[list[int]]


def dfs(node: int, dist: int, depth: int) -> None:
    depth_list[node] = depth
    distance_list[node] = dist
    for next_node, next_dist in edge_list[node]:
        if depth_list[next_node] == -1:
            parent_list[next_node][0] = node
            dfs(next_node, dist + next_dist, depth + 1)


def set_parent(n: int) -> None:
    global depth_list, distance_list, parent_list
    depth_list = [-1 for _ in range(n + 1)]
    distance_list = [0 for _ in range(n + 1)]
    parent_list = [[-1 for _ in range(LOG)] for _ in range(n + 1)]

    dfs(1, 0, 0)
    for i in range(1, LOG):
        for node in range(1, n + 1):
            parent_list[node][i] = parent_list[parent_list[node][i - 1]][i - 1]


def find_common_parent(node1: int, node2: int) -> int:
    if depth_list[node1] > depth_list[node2]:
        node1, node2 = node2, node1
    for i in range(LOG - 1, -1, -1):
        if depth_list[node2] - depth_list[node1] >= (1 << i):
            node2 = parent_list[node2][i]
    if node1 == node2:
        return node1
    for i in range(LOG - 1, -1, -1):
        if parent_list[node1][i] != parent_list[node2][i]:
            node1 = parent_list[node1][i]
            node2 = parent_list[node2][i]
    return parent_list[node1][0]


def main() -> None:
    global edge_list, depth_list, distance_list, parent_list
    n = int(input())

    edge_list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        node1, node2, dist = map(int, input().split())
        edge_list[node1].append((node2, dist))
        edge_list[node2].append((node1, dist))

    set_parent(n)

    m = int(input())
    for _ in range(m):
        node1, node2 = map(int, input().split())
        parent = find_common_parent(node1, node2)
        print(distance_list[node1] + distance_list[node2] - 2 * distance_list[parent])


if __name__ == "__main__":
    sys.setrecursionlimit(50000)
    main()
