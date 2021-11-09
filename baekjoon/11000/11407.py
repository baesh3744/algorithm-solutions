import sys
from collections import deque
from typing import List, Tuple


INF = sys.maxsize

input = sys.stdin.readline


def spfa() -> List[int]:
    cost_list: List[int] = [INF for _ in range(sink + 1)]
    prev_list: List[int] = [-1 for _ in range(sink + 1)]
    in_que: List[bool] = [False for _ in range(sink + 1)]
    que: deque[int] = deque()

    cost_list[source] = 0
    in_que[source] = True
    que.append(source)

    while que:
        node = que.popleft()
        in_que[node] = False

        for adj_node in adj_list[node]:
            cost: int = cost_network[node][adj_node]

            if (
                cap_network[node][adj_node] - flow_network[node][adj_node] > 0
                and cost_list[adj_node] > cost_list[node] + cost
            ):
                cost_list[adj_node] = cost_list[node] + cost
                prev_list[adj_node] = node
                if not in_que[adj_node]:
                    in_que[adj_node] = True
                    que.append(adj_node)

    return prev_list


def find_flow(prev_list: List[int]) -> int:
    cur: int = sink
    flow: int = INF
    while cur != source:
        prev: int = prev_list[cur]
        flow = min(flow, cap_network[prev][cur] - flow_network[prev][cur])
        cur = prev
    return flow


def update_network(flow: int, prev_list: List[int]) -> int:
    cost: int = 0
    cur: int = sink
    while cur != source:
        prev: int = prev_list[cur]
        cost += flow * cost_network[prev][cur]
        flow_network[prev][cur] += flow
        flow_network[cur][prev] -= flow
        cur = prev
    return cost


def mcmf() -> Tuple[int, int]:
    _cnt: int = 0
    _max_cost: int = 0
    while True:
        prev_list = spfa()
        if prev_list[sink] == -1:
            break
        flow = find_flow(prev_list)
        _cnt += flow
        _max_cost += update_network(flow, prev_list)
    return _cnt, _max_cost


if __name__ == "__main__":
    n, m = map(int, input().split())

    source: int = m + n
    sink: int = m + n + 1
    adj_list: List[List[int]] = [[] for _ in range(sink + 1)]
    cap_network: List[List[int]] = [
        [0 for _ in range(sink + 1)] for _ in range(sink + 1)
    ]
    cost_network: List[List[int]] = [
        [0 for _ in range(sink + 1)] for _ in range(sink + 1)
    ]
    flow_network: List[List[int]] = [
        [0 for _ in range(sink + 1)] for _ in range(sink + 1)
    ]

    a = list(map(int, input().split()))
    for person in range(m, source):
        adj_list[person].append(sink)
        adj_list[sink].append(person)
        cap_network[person][sink] += a[person - m]

    b = list(map(int, input().split()))
    for bookstore in range(m):
        adj_list[bookstore].append(source)
        adj_list[source].append(bookstore)
        cap_network[source][bookstore] += b[bookstore]

    c = [list(map(int, input().split())) for _ in range(m)]
    d = [list(map(int, input().split())) for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if c[i][j] == 0:
                continue

            bookstore, person = i, m + j

            adj_list[bookstore].append(person)
            adj_list[person].append(bookstore)

            cost_network[bookstore][person] += d[i][j]
            cost_network[person][bookstore] -= d[i][j]

            cap_network[bookstore][person] += c[i][j]

    cnt, max_cost = mcmf()
    print(cnt)
    print(max_cost)
