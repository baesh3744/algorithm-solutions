import sys


def get_xor(start: int, end: int) -> int:
    if start > end:
        return 0
    if start == end:
        return records[start]
    if cache[start][end] != -1:
        return cache[start][end]

    cache[start][end] = records[end] ^ get_xor(start, end - 1)
    return cache[start][end]


def main() -> None:
    global records, cache
    n, q = map(int, input().split())
    records = list(map(int, input().split()))

    cache = [[-1 for _ in range(n)] for _ in range(n)]
    for _ in range(q):
        inputs = list(map(int, sys.stdin.readline().split()))
        if inputs[0] == 0:
            _, x, y = inputs
            print(get_xor(x - 1, y - 2))
        else:
            _, x, y, d = inputs
            print(get_xor(x - 1, y - 2) ^ d)


if __name__ == "__main__":
    main()
