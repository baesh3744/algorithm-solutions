import itertools
import sys
from typing import List


def combine_two_weights(weight_a: List[int], weight_b: List[int]) -> List[int]:
    combined: List[int] = []
    for a, b in itertools.product(weight_a, weight_b):
        combined.append(a + b)
    return list(set(sorted(combined)))


def get_nearest_total(k: int,
                      wt: int,
                      length: int,
                      weights34: List[int]) -> int:
    start: int = 0
    end: int = length - 1

    while start <= end:
        mid: int = (start + end) // 2
        if wt + weights34[mid] <= k:
            start = mid + 1
        else:
            end = mid - 1

    if end == -1:
        end = 0

    if (end + 1 < length and
            (wt + weights34[end + 1]) - k < k - (wt + weights34[end])):
        end += 1

    return wt + weights34[end]


def get_canoe_weight(k: int, weights: List[List[int]]) -> int:
    weights12 = combine_two_weights(weights[0], weights[1])
    weights34 = combine_two_weights(weights[2], weights[3])

    min_diff = sys.maxsize
    total = sys.maxsize
    length: int = len(weights34)

    for wt in weights12:
        nearest_total = get_nearest_total(k, wt, length, weights34)
        diff = abs(nearest_total - k)

        if diff < min_diff:
            min_diff = diff
            total = nearest_total
        elif diff == min_diff:
            total = min(total, nearest_total)

    return total


def main() -> None:
    t = int(input())
    for _ in range(t):
        k, _ = map(int, input().split())
        weights = [list(map(int, input().split())) for _ in range(4)]
        print(get_canoe_weight(k, weights))


if __name__ == "__main__":
    main()
