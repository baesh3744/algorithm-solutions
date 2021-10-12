import heapq


def get_stone(t: int, p: int, k: list[int]) -> int:
    heap: list[int] = []
    for stone in k:
        heapq.heappush(heap, -stone)
        t -= stone + p
        if t < 0:
            t -= heapq.heappop(heap)
    return len(heap)


def main() -> None:
    _, t, p = map(int, input().split())
    k = list(map(int, input().split()))

    print(get_stone(t + p, p, k))


if __name__ == "__main__":
    main()
