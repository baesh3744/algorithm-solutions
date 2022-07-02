import sys


input = sys.stdin.readline


def lcs(x: str, y: str) -> int:
    x_length, y_length = len(x), len(y)
    cache = [[0 for _ in range(y_length + 1)] for _ in range(x_length + 1)]

    for x_index in range(1, x_length + 1):
        for y_index in range(1, y_length + 1):
            match = int(x[x_index - 1] == y[y_index - 1])

            cache[x_index][y_index] = max(
                cache[x_index - 1][y_index],
                cache[x_index][y_index - 1],
                cache[x_index - 1][y_index - 1] + match,
            )

    return cache[x_length][y_length]


def main() -> None:
    x = input().strip()
    y = input().strip()

    print(lcs(x, y))


if __name__ == "__main__":
    main()
