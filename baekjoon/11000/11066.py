import sys
from typing import List


cache: List[List[int]] = []
combined_file: List[List[int]] = []
file_sizes: List[int] = []


def combine_file(k: int) -> None:
    global combined_file
    combined_file = [[0 for _ in range(k)] for _ in range(k)]
    for sidx in range(k):
        sub_sum: int = 0
        for eidx in range(sidx, k):
            sub_sum += file_sizes[eidx]
            combined_file[sidx][eidx] = sub_sum


def get_combined_cost(start: int, end: int) -> int:
    if start == end:
        return 0
    if start + 1 == end:
        return combined_file[start][end]
    if cache[start][end] != -1:
        return cache[start][end]

    min_cost: int = sys.maxsize
    for mid in range(start, end):
        cost: int = get_combined_cost(start, mid) + \
            get_combined_cost(mid + 1, end) + \
            combined_file[start][mid] + \
            combined_file[mid + 1][end]
        min_cost = min(min_cost, cost)
    cache[start][end] = min_cost
    return cache[start][end]


def main() -> None:
    global file_sizes, cache
    t = int(input())
    for _ in range(t):
        k = int(sys.stdin.readline())
        file_sizes = list(map(int, sys.stdin.readline().split()))

        cache = [[-1 for _ in range(k)] for _ in range(k)]
        combine_file(k)
        print(get_combined_cost(0, k - 1))


if __name__ == "__main__":
    main()
