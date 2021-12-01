import sys
from typing import List


input = sys.stdin.readline


def get_length(start: int, end: int) -> int:
    if start >= end:
        return 0
    if cache[start][end] != -1:
        return cache[start][end]

    max_length: int = 0

    if ((dna[start], dna[end]) == ("a", "t")) or ((dna[start], dna[end]) == ("g", "c")):
        max_length = max(max_length, 2 + get_length(start + 1, end - 1))

    for idx in range(start, end):
        max_length = max(max_length, get_length(start, idx) + get_length(idx + 1, end))

    cache[start][end] = max_length
    return max_length


if __name__ == "__main__":
    dna = input().strip()

    length: int = len(dna)
    cache: List[List[int]] = [[-1 for _ in range(length)] for _ in range(length)]
    print(get_length(0, length - 1))
