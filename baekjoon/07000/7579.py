def knapsack(capacity: int, n: int, memories: list[int], costs: list[int]) -> int:
    total_cost: int = sum(costs)
    cache: list[int] = [0 for _ in range(total_cost + 1)]
    min_cost: int = total_cost

    for idx in range(n):
        for cost in range(total_cost, costs[idx] - 1, -1):
            cache[cost] = max(cache[cost],
                              cache[cost - costs[idx]] + memories[idx])
            if cache[cost] >= capacity:
                min_cost = min(min_cost, cost)

    return min_cost


def main() -> None:
    n, m = map(int, input().split())
    memories = list(map(int, input().split()))
    costs = list(map(int, input().split()))

    print(knapsack(m, n, memories, costs))


if __name__ == "__main__":
    main()
