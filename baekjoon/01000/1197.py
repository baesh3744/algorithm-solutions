import sys


input = sys.stdin.readline

parent: dict[int, int] = {}
rank: dict[int, int] = {}


def make_set(v: int) -> None:
    for node in range(1, v+1):
        parent[node] = node
        rank[node] = 0


def find(node: int) -> int:
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_u: int, node_v: int) -> None:
    root_u, root_v = find(node_u), find(node_v)
    if rank[root_u] > rank[root_v]:
        parent[root_v] = root_u
    else:
        parent[root_u] = root_v
        if rank[root_u] == rank[root_v]:
            rank[root_v] += 1


def kruskal(v: int, edges: list[tuple[int, int, int]]) -> int:
    mst_weight: int = 0

    make_set(v)

    sorted_edges = sorted(edges, key=lambda x: x[2])

    for edge in sorted_edges:
        node_u, node_v, weight = edge
        if find(node_u) != find(node_v):
            union(node_u, node_v)
            mst_weight += weight

    return mst_weight


def main() -> None:
    v, e = map(int, input().split())
    edges = [tuple[int, int, int](map(int, input().split())) for _ in range(e)]

    print(kruskal(v, edges))


if __name__ == "__main__":
    main()
