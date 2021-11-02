import sys
from collections import deque


MAX = sys.maxsize
SINK = 1

input = sys.stdin.readline


def find_min_flow(prev_list: list[int]) -> int:
    flow: int = MAX
    cur: int = SINK
    while cur != source:
        prev: int = prev_list[cur]
        flow = min(flow, capacity_network[prev][cur] - flow_network[prev][cur])
        cur = prev
    return flow


def update_network(flow: int, prev_list: list[int]) -> None:
    cur: int = SINK
    while cur != source:
        prev: int = prev_list[cur]
        flow_network[prev][cur] += flow
        flow_network[cur][prev] -= flow
        cur = prev


def bfs() -> int:
    prev_list: list[int] = [-1 for _ in range(2 * n)]
    que: deque[int] = deque([source])
    while que:
        city: int = que.popleft()
        for adj_city in adj_list[city]:
            if (
                prev_list[adj_city] == -1
                and capacity_network[city][adj_city] - flow_network[city][adj_city] > 0
            ):
                que.append(adj_city)
                prev_list[adj_city] = city
                if adj_city == SINK:
                    flow = find_min_flow(prev_list)
                    update_network(flow, prev_list)
                    return flow
    return -1


def edmonds_karp() -> int:
    max_cnt: int = 0
    while True:
        flow = bfs()
        if flow == -1:
            break
        max_cnt += 1
    return max_cnt


if __name__ == "__main__":
    n, p = map(int, input().split())

    source: int = n
    adj_list: list[list[int]] = [[] for _ in range(2 * n)]
    flow_network: list[list[int]] = [[0 for _ in range(2 * n)] for _ in range(2 * n)]
    capacity_network: list[list[int]] = [
        [0 for _ in range(2 * n)] for _ in range(2 * n)
    ]

    for city in range(n):
        adj_list[city].append(city + n)
        adj_list[city + n].append(city)
        capacity_network[city][city + n] = 1

    for _ in range(p):
        u, v = map(lambda x: int(x) - 1, input().split())

        adj_list[u + n].append(v)
        adj_list[v].append(u + n)
        capacity_network[u + n][v] = 1

        adj_list[v + n].append(u)
        adj_list[u].append(v + n)
        capacity_network[v + n][u] = 1

    print(edmonds_karp())
