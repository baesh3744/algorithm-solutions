import sys
from itertools import combinations


BASE = {"a", "c", "i", "n", "t"}

input = sys.stdin.readline


def pre() -> tuple[set[int], list[int]]:
    alphabets: set[int] = set()
    bitwords: list[int] = [0 for _ in range(n)]

    for idx, word in enumerate(words):
        for char in word:
            if char in BASE:
                continue

            intchar = 1 << (ord(char) - 97)
            alphabets.add(intchar)
            bitwords[idx] |= intchar

    return alphabets, bitwords


def count_readable() -> int:
    alphabets, bitwords = pre()

    max_readable: int = 0
    for comb in combinations(alphabets, min(len(alphabets), k - 5)):
        learned: int = sum(comb)
        readable: int = sum(1 for word in bitwords if word & learned == word)
        max_readable = max(max_readable, readable)
    return max_readable


if __name__ == "__main__":
    n, k = map(int, input().split())
    words = [set(input().strip()) for _ in range(n)]

    print(count_readable() if k >= 5 else 0)
