import heapq
import sys


input = sys.stdin.readline

upper: list[int] = []
lower: list[int] = []


def add_number(num: int) -> None:
    if len(upper) == len(lower):
        if upper:
            tmp = heapq.heappop(upper)
            if tmp < num:
                tmp, num = num, tmp
            heapq.heappush(upper, tmp)
        heapq.heappush(lower, -num)
    else:
        if lower:
            tmp = -heapq.heappop(lower)
            if tmp < num:
                tmp, num = num, tmp
            heapq.heappush(upper, tmp)
        heapq.heappush(lower, -num)


def main() -> None:
    n = int(input())

    for _ in range(n):
        add_number(int(input()))
        print(-lower[0])


if __name__ == "__main__":
    main()
