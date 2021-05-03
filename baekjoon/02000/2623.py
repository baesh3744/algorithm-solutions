from collections import deque


indegrees: list[int] = []
graph: list[list[int]] = []
orders: list[int] = []


def make_graph(n: int, orders_input: list[list[int]]) -> None:
    global indegrees, graph

    indegrees = [0] * (n + 1)
    graph = [[] for _ in range(n + 1)]

    for order in orders_input:
        for idx in range(1, len(order) - 1):
            node_from: int = order[idx]
            node_to: int = order[idx + 1]

            graph[node_from].append(node_to)
            indegrees[node_to] += 1


def get_order() -> bool:
    que: deque[int] = deque()

    for idx in range(len(indegrees)):
        if idx != 0 and indegrees[idx] == 0:
            que.append(idx)

    while que:
        cur = que.popleft()
        orders.append(cur)

        for next in graph[cur]:
            indegrees[next] -= 1

            if indegrees[next] == 0:
                que.append(next)

    if any(indegrees):
        return False
    return True


def main() -> None:
    n, m = map(int, input().split())
    orders_input = [list(map(int, input().split())) for _ in range(m)]

    make_graph(n, orders_input)

    if get_order():
        for order in orders:
            print(order)
    else:
        print('0')


if __name__ == "__main__":
    main()
