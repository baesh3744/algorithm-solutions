import sys
from collections import deque
from typing import List, Tuple


MAX = sys.maxsize

input = sys.stdin.readline


def spfa() -> List[int]:
    cost_list: List[int] = [MAX for _ in range(cnt_node)]
    in_queue: List[bool] = [False for _ in range(cnt_node)]
    prev_list: List[int] = [-1 for _ in range(cnt_node)]
    que: deque[int] = deque()

    cost_list[source] = 0
    in_queue[source] = True
    que.append(source)

    while que:
        node = que.popleft()
        in_queue[node] = False

        for adj_node in adj_list[node]:
            if (
                cap_network[node][adj_node] - flow_network[node][adj_node] > 0
                and cost_list[adj_node] > cost_list[node] + cost_network[node][adj_node]
            ):
                cost_list[adj_node] = cost_list[node] + cost_network[node][adj_node]
                prev_list[adj_node] = node
                if not in_queue[adj_node]:
                    in_queue[adj_node] = True
                    que.append(adj_node)

    return prev_list


def find_min_flow(prev_list: List[int]) -> int:
    cur: int = sink
    min_flow: int = MAX
    while cur != source:
        prev: int = prev_list[cur]
        min_flow = min(min_flow, cap_network[prev][cur] - flow_network[prev][cur])
        cur = prev
    return min_flow


def update_flow_network(flow: int, prev_list: List[int]) -> int:
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
    cnt: int = 0
    max_cost: int = 0
    while True:
        prev_list = spfa()
        if prev_list[sink] == -1:
            break
        min_flow = find_min_flow(prev_list)
        cost = update_flow_network(min_flow, prev_list)
        cnt += min_flow
        max_cost += cost
    return cnt, max_cost


if __name__ == "__main__":
    n, m = map(int, input().split())

    source, sink = 0, n + m + 1
    cnt_node = sink + 1
    adj_list: List[List[int]] = [[] for _ in range(cnt_node)]
    cap_network: List[List[int]] = [
        [0 for _ in range(cnt_node)] for _ in range(cnt_node)
    ]
    cost_network: List[List[int]] = [
        [0 for _ in range(cnt_node)] for _ in range(cnt_node)
    ]
    flow_network: List[List[int]] = [
        [0 for _ in range(cnt_node)] for _ in range(cnt_node)
    ]

    for person in range(1, n + 1):
        adj_list[source].append(person)
        adj_list[person].append(source)
        cap_network[source][person] = 1

    for work in range(n + 1, sink):
        adj_list[sink].append(work)
        adj_list[work].append(sink)
        cap_network[work][sink] = 1

    for person in range(1, n + 1):
        cnt, *work_list = map(int, input().split())
        for idx in range(cnt):
            work: int = work_list[2 * idx] + n
            cost: int = work_list[2 * idx + 1]

            adj_list[person].append(work)
            adj_list[work].append(person)

            cost_network[person][work] = cost
            cost_network[work][person] = -cost

            cap_network[person][work] = 1

    cnt, cost = mcmf()
    print(cnt)
    print(cost)
