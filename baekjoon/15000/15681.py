import sys


input = sys.stdin.readline


def count_subnodes(node: int, edges: list[list[int]], visited: list[bool]) -> None:
    """
    tree[node]에 서브 트리에 속한 정점의 수를 기록한다.
    """
    visited[node] = True
    for subnode in edges[node]:
        if visited[subnode]:
            continue
        count_subnodes(subnode, edges, visited)
        tree[node] += tree[subnode]


def main() -> None:
    global tree
    n, r, q = map(int, input().split())

    edges: list[list[int]] = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        edges[u].append(v)
        edges[v].append(u)

    tree = [1 for _ in range(n + 1)]
    visited = [False for _ in range(n + 1)]
    count_subnodes(r, edges, visited)

    for _ in range(q):
        node = int(input())
        print(tree[node])


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
