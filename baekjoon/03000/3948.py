import sys
from math import comb


input = sys.stdin.readline


def count(n: int) -> int:
    if n <= 1:
        return 1
    if cache[n] != -1:
        return cache[n]

    cnt: int = 0
    for k in range(n):
        cnt += comb(n - 1, k) * count(k) * count(n - k - 1)
    cache[n] = cnt // 2
    return cache[n]


if __name__ == "__main__":
    t = int(input())

    cache = [-1 for _ in range(21)]
    for _ in range(t):
        n = int(input())

        if n == 1:
            print(1)
        else:
            print(2 * count(n))
