import sys


input = sys.stdin.readline

stack: list[int] = []
edge_list: list[list[int]]


def initialize(length: int) -> None:
    global _id, scc_id, finished, id_list, sccid_list, edge_list
    _id = 0
    scc_id = 1
    finished = [False for _ in range(length)]
    id_list = [-1 for _ in range(length)]
    sccid_list = [-1 for _ in range(length)]
    edge_list = [[] for _ in range(length)]


def dfs(x: int) -> int:
    global _id, scc_id
    _id += 1
    id_list[x] = _id
    stack.append(x)

    parent: int = id_list[x]
    for nx in edge_list[x]:
        if id_list[nx] == -1:
            parent = min(parent, dfs(nx))
        elif not finished[nx]:
            parent = min(parent, id_list[nx])

    if parent == id_list[x]:
        while True:
            top = stack.pop()
            sccid_list[top] = scc_id
            finished[top] = True
            if top == x:
                break
        scc_id += 1

    return parent


def check(n: int) -> bool:
    for x in range(1, n + 1):
        if sccid_list[x] == sccid_list[-x]:
            return False
    return True


def print_answer(n: int) -> None:
    can_true = check(n)
    print(int(can_true))
    if can_true:
        for x in range(1, n + 1):
            print(int(sccid_list[x] < sccid_list[-x]), end=" ")


def main() -> None:
    n, m = map(int, input().split())

    initialize(2 * n + 1)

    for _ in range(m):
        x, y = map(int, input().split())
        edge_list[-x].append(y)
        edge_list[-y].append(x)

    for x in range(1, 2 * n + 1):
        if id_list[x] == -1:
            dfs(x)

    print_answer(n)


if __name__ == "__main__":
    sys.setrecursionlimit(20000)
    main()
