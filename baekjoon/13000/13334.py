import heapq
import sys


input = sys.stdin.readline


def main() -> None:
    n = int(input())
    locations = [sorted(map(int, input().split())) for _ in range(n)]
    l = int(input())

    locations.sort(key=lambda x: -x[1], reverse=True)

    ans: int = 0
    heap: list[int] = []
    for h, o in locations:
        if o - h > l:
            continue

        while heap and heap[0] + l < o:
            heapq.heappop(heap)
        heapq.heappush(heap, h)
        ans = max(ans, len(heap))

    print(ans)


if __name__ == "__main__":
    main()
