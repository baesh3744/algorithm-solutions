import sys


input = sys.stdin.readline

dsc_number: int
discovered: list[int]
abridge_list: list[list[int]]
edge_list: list[list[int]]


def initialize(v: int) -> None:
    global dsc_number, abridge_list, discovered, edge_list
    dsc_number = 1
    discovered = [-1 for _ in range(v + 1)]
    abridge_list = []
    edge_list = [[] for _ in range(v + 1)]


def dfs(node: int, parent: int) -> int:
    global dsc_number
    discovered[node] = dsc_number
    dsc_number += 1

    ret: int = discovered[node]
    for adj_node in edge_list[node]:
        if adj_node == parent:
            continue

        if discovered[adj_node] != -1:
            ret = min(ret, discovered[adj_node])
            continue

        adj: int = dfs(adj_node, node)
        if adj > discovered[node]:
            abridge_list.append([node, adj_node])
        ret = min(ret, adj)

    return ret


def print_abridge() -> None:
    print(len(abridge_list))
    for a, b in sorted(map(lambda x: sorted(x), abridge_list)):
        print(a, b)


def main() -> None:
    v, e = map(int, input().split())

    initialize(v)

    for _ in range(e):
        a, b = map(int, input().split())
        edge_list[a].append(b)
        edge_list[b].append(a)

    for node in range(1, v + 1):
        if discovered[node] == -1:
            dfs(node, 0)

    print_abridge()


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()
