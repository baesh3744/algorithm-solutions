import heapq
import sys


input = sys.stdin.readline


def get_max_jewel_cost(
    n: int, jewels: list[tuple[int, int]], capacities: list[int]
) -> int:
    jindex, cost = 0, 0
    heap: list[int] = []

    for capacity in capacities:
        while jindex < n and jewels[jindex][0] <= capacity:
            heapq.heappush(heap, (-1 * jewels[jindex][1]))
            jindex += 1

        if heap:
            cost += -1 * heapq.heappop(heap)

    return cost


def main() -> None:
    n, k = map(int, input().split())
    jewels = [tuple[int, int](map(int, input().split())) for _ in range(n)]
    capacities = [int(input()) for _ in range(k)]

    print(get_max_jewel_cost(n, k, sorted(jewels), sorted(capacities)))


if __name__ == "__main__":
    main()
