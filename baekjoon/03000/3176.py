import sys
from typing import List, Tuple


LOG: int = 18
MAX: int = sys.maxsize

input = sys.stdin.readline

edge_list: List[List[Tuple[int, int]]]
depth_list: List[int]
max_list: List[List[int]]
min_list: List[List[int]]
parent_list: List[List[int]]


def initialize(n: int) -> None:
    global depth_list, max_list, min_list, parent_list
    depth_list = [-1 for _ in range(n + 1)]
    max_list = [[-1 for _ in range(LOG)] for _ in range(n + 1)]
    min_list = [[MAX for _ in range(LOG)] for _ in range(n + 1)]
    parent_list = [[-1 for _ in range(LOG)] for _ in range(n + 1)]


def dfs(node: int, depth: int) -> None:
    depth_list[node] = depth
    for child, dist in edge_list[node]:
        if depth_list[child] == -1:
            max_list[child][0] = dist
            min_list[child][0] = dist
            parent_list[child][0] = node
            dfs(child, depth + 1)


def set_lists(n: int) -> None:
    initialize(n)

    dfs(1, 0)
    for i in range(1, LOG):
        for node in range(2, n + 1):
            parent: int = parent_list[node][i - 1]
            max_list[node][i] = max(max_list[node][i - 1], max_list[parent][i - 1])
            min_list[node][i] = min(min_list[node][i - 1], min_list[parent][i - 1])
            parent_list[node][i] = parent_list[parent][i - 1]


def solve(d: int, e: int) -> Tuple[int, int]:
    _max, _min = -1, MAX
    if depth_list[d] > depth_list[e]:
        d, e = e, d
    for i in range(LOG - 1, -1, -1):
        if depth_list[e] - depth_list[d] >= (1 << i):
            _max = max(_max, max_list[e][i])
            _min = min(_min, min_list[e][i])
            e = parent_list[e][i]
    if d == e:
        return _max, _min
    for i in range(LOG - 1, -1, -1):
        if parent_list[d][i] != parent_list[e][i]:
            _max = max(_max, max_list[d][i], max_list[e][i])
            _min = min(_min, min_list[d][i], min_list[e][i])
            d = parent_list[d][i]
            e = parent_list[e][i]
    _max = max(_max, max_list[d][0], max_list[e][0])
    _min = min(_min, min_list[d][0], min_list[e][0])
    return _max, _min


def main() -> None:
    global edge_list
    n = int(input())

    edge_list = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b, c = map(int, input().split())
        edge_list[a].append((b, c))
        edge_list[b].append((a, c))

    set_lists(n)

    k = int(input())
    for _ in range(k):
        d, e = map(int, input().split())
        _max, _min = solve(d, e)
        print(_min, _max)


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
