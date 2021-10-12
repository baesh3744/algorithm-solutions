import sys


input = sys.stdin.readline

id_: int
scc_num: int
finished: list[bool]
id_list: list[int]
sccid_list: list[int]
stack: list[int]
graph: list[set[int]]


def initialize(length: int) -> None:
    global id_, scc_num, finished, id_list, sccid_list, stack
    id_ = 0
    scc_num = 1
    finished = [False for _ in range(length)]
    id_list = [0 for _ in range(length)]
    sccid_list = [0 for _ in range(length)]
    stack = []


def dfs(node: int) -> int:
    global id_, scc_num
    id_ += 1
    id_list[node] = id_
    stack.append(node)

    parent: int = id_list[node]
    for next_node in graph[node]:
        if id_list[next_node] == 0:
            parent = min(parent, dfs(next_node))
        elif not finished[next_node]:
            parent = min(parent, id_list[next_node])

    if parent == id_list[node]:
        while True:
            top: int = stack.pop()
            finished[top] = True
            sccid_list[top] = scc_num
            if top == node:
                break
        scc_num += 1

    return parent


def main() -> None:
    global graph
    n, m = map(int, input().split())

    graph = [set([]) for _ in range(2 * n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[-x].add(y)
        graph[-y].add(x)

    initialize(2 * n + 1)

    for node in range(1, n + 1):
        if id_list[node] == 0:
            dfs(node)

    can_true: bool = True
    for node in range(1, n + 1):
        if sccid_list[node] == sccid_list[-node]:
            can_true = False
            break
    print(int(can_true))


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    main()
