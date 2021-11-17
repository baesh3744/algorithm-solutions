import sys
from heapq import heappop, heappush
from typing import List, Tuple


input = sys.stdin.readline


def getd() -> List[int]:
    d = [0 for _ in range(n)]
    heap: List[Tuple[int, int]] = []

    for idx, value in enumerate(a):
        heappush(heap, (value, idx))

        while True:
            min_value, min_idx = heappop(heap)
            if idx - l + 1 <= min_idx:
                d[idx] = min_value
                heappush(heap, (min_value, min_idx))
                break

    return d


if __name__ == "__main__":
    n, l = map(int, input().split())
    a = list(map(int, input().split()))

    print(" ".join(map(str, getd())))
