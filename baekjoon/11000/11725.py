import sys


links: dict[int, list[int]] = {}
parents: list[int] = []


def update_parents(node: int) -> None:
    for child in links[node]:
        if parents[child] == -1:
            parents[child] = node
            update_parents(child)


def main() -> None:
    global links, parents
    n = int(input())

    links = {node: [] for node in range(1, n + 1)}
    for _ in range(n - 1):
        node1, node2 = map(int, sys.stdin.readline().split())
        links[node1].append(node2)
        links[node2].append(node1)

    parents = [-1 for _ in range(n + 1)]
    update_parents(1)

    for node in range(2, n + 1):
        print(parents[node])


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
