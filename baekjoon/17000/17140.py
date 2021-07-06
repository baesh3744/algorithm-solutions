from collections import Counter
from itertools import repeat


Array = list[list[int]]


def count_values(a: Array) -> Array:
    for ridx, row in enumerate(a):
        counter = sorted(Counter(row).items(), key=lambda x: (x[1], x[0]))
        a[ridx] = [it for items in counter if items[0] != 0 for it in items]
    return a


def get_max_len(a: Array) -> int:
    max_len: int = 0
    for row in a:
        max_len = max(max_len, len(row))
    return max_len


def resize_array(a: Array) -> Array:
    length = get_max_len(a)
    for ridx, row in enumerate(a):
        a[ridx] = (row + list(repeat(0, length - len(row))))[:100]
    return a


def calculate(ridx: int, cidx: int, k: int, a: Array) -> int:
    for time in range(101):
        rlen: int = len(a)
        clen: int = len(a[0])

        if ridx < rlen and cidx < clen and a[ridx][cidx] == k:
            return time

        if rlen >= clen:
            a = resize_array(count_values(a))
        else:
            a = list(map(list[int], zip(*a)))
            a = resize_array(count_values(a))
            a = list(map(list[int], zip(*a)))

    return -1


def main() -> None:
    r, c, k = map(int, input().split())
    a = [list(map(int, input().split())) for _ in range(3)]

    print(calculate(r - 1, c - 1, k, a))


if __name__ == "__main__":
    main()
