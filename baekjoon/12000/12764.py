import sys
from heapq import heappop, heappush


input = sys.stdin.readline


def count(n: int, times: list[tuple[int, int]]) -> tuple[int, list[int]]:
    x: int = 0
    people: list[int] = [0 for _ in range(n + 1)]
    computers: list[int] = []
    heap: list[tuple[int, int]] = []

    for start, end in sorted(times):
        while heap and heap[0][0] <= start:
            _, com = heappop(heap)
            heappush(computers, com)

        if computers:
            com = heappop(computers)
        else:
            x += 1
            com = x

        people[com] += 1
        heappush(heap, (end, com))

    return x, people[1 : x + 1]


if __name__ == "__main__":
    n = int(input())

    times: list[tuple[int, int]] = [
        tuple[int, int](map(int, input().split())) for _ in range(n)
    ]

    x, people = count(n, times)
    print(x)
    print(" ".join(map(str, people)))
