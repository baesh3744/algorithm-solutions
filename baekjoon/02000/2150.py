import sys


input = sys.stdin.readline

id_: int
id_list: list[int]
stack: list[int]
finished: list[bool]
edge_list: list[list[int]]
scc_list: list[list[int]]


def add_scc(node: int) -> int:
    global id_, id_list, stack, finished, edge_list, scc_list
    id_ += 1
    id_list[node] = id_
    stack.append(node)

    parent: int = id_list[node]
    for next_node in edge_list[node]:
        if id_list[next_node] == -1:
            parent = min(parent, add_scc(next_node))
        elif not finished[next_node]:
            parent = min(parent, id_list[next_node])

    if parent == id_list[node]:
        scc: list[int] = []
        while True:
            prev = stack.pop()
            scc.append(prev)
            finished[prev] = True
            if prev == node:
                break
        scc_list.append(scc)

    return parent


def main() -> None:
    global id_, id_list, stack, finished, edge_list, scc_list
    v, e = map(int, input().split())

    edge_list = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        edge_list[a].append(b)

    id_ = 0
    id_list = [-1 for _ in range(v + 1)]
    stack = []
    finished = [False for _ in range(v + 1)]
    scc_list = []

    for node in range(1, v + 1):
        if id_list[node] == -1:
            add_scc(node)

    scc_list = sorted(sorted(scc) for scc in scc_list)
    print(len(scc_list))
    for scc in scc_list:
        print(" ".join(map(str, scc + [-1])))


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    main()
