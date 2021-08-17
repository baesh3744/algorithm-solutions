import sys


input = sys.stdin.readline

cache: list[list[int]]
graph: list[list[int]]


def count_early(node: int, is_early: int, visited: list[bool]) -> int:
    if cache[node][is_early] != -1:
        return cache[node][is_early]

    cnt: int = is_early
    for connected in graph[node]:
        if visited[connected]:
            continue
        visited[connected] = True
        if is_early == 0:
            cnt += count_early(connected, 1, visited)
        else:
            cnt += min(
                count_early(connected, 0, visited),
                count_early(connected, 1, visited),
            )
        visited[connected] = False
    cache[node][is_early] = cnt
    return cache[node][is_early]


def main() -> None:
    global cache, graph
    n = int(input())

    graph = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cache = [[-1] * 2 for _ in range(n + 1)]
    visited: list[bool] = [False for _ in range(n + 1)]
    visited[1] = True
    print(min(count_early(1, 0, visited), count_early(1, 1, visited)))


if __name__ == "__main__":
    sys.setrecursionlimit(2000000)
    main()
