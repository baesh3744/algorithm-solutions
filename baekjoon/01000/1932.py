import sys


input = sys.stdin.readline


def sum(height: int, index: int) -> int:
    if height == n - 1:
        return numbers[height][index]
    if cache[height][index] != -1:
        return cache[height][index]

    cache[height][index] = numbers[height][index] + max(
        sum(height + 1, index), sum(height + 1, index + 1)
    )
    return cache[height][index]


def main() -> None:
    global n, numbers, cache
    n = int(input())
    numbers = [list(map(int, input().split())) for _ in range(n)]

    cache = [[-1 for _ in range(n)] for _ in range(n)]
    print(sum(0, 0))


if __name__ == "__main__":
    main()
