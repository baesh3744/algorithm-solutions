import sys


input = sys.stdin.readline

graph: list[list[int]]


def count_early(node: int, parent: int) -> bool:
    global total
    cnt_children: int = len(graph[node]) - 1
    if cnt_children == -1:
        return False

    cnt_early: int = 0
    for connected in graph[node]:
        if connected != parent and count_early(connected, node):
            cnt_early += 1

    if cnt_early == cnt_children:
        return False
    total += 1
    return True


def main() -> None:
    global graph, total
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    graph[1].append(0)
    total = 0
    count_early(1, 0)
    print(total)


if __name__ == "__main__":
    sys.setrecursionlimit(2000000)
    main()
