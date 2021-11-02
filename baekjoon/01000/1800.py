import sys
from heapq import heappush, heappop


MAX = sys.maxsize

input = sys.stdin.readline

cables: list[list[tuple[int, int]]]


def dijkstra(pivot: int) -> int:
    weights: list[int] = [MAX for _ in range(n + 1)]
    heap: list[tuple[int, int]] = []

    weights[1] = 0
    heappush(heap, (0, 1))

    while heap:
        dist, computer = heappop(heap)
        if dist > weights[computer]:
            continue

        for adj_computer, adj_cost in cables[computer]:
            adj_dist: int = dist + (1 if adj_cost > pivot else 0)
            if adj_dist < weights[adj_computer]:
                weights[adj_computer] = adj_dist
                heappush(heap, (adj_dist, adj_computer))

    return weights[n]


def get_cost_to_pay(costs: list[int]) -> int:
    if dijkstra(0) <= k:
        return 0

    start, end = 0, p - 1
    while start <= end:
        mid: int = (start + end) // 2
        weight: int = dijkstra(costs[mid])
        if weight <= k:
            end = mid - 1
        else:
            start = mid + 1
    return costs[start] if start < p else -1


def main() -> None:
    global n, p, k, cables
    n, p, k = map(int, input().split())

    costs: list[int] = []
    cables = [[] for _ in range(n + 1)]
    for _ in range(p):
        c1, c2, cost = map(int, input().split())
        cables[c1].append((c2, cost))
        cables[c2].append((c1, cost))
        costs.append(cost)

    print(get_cost_to_pay(sorted(costs)))


if __name__ == "__main__":
    main()
