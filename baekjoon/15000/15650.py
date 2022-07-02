import sys
from itertools import combinations


input = sys.stdin.readline


def main() -> None:
    n, m = map(int, input().split())
    for numbers in combinations(range(1, n + 1), m):
        print(" ".join(map(str, numbers)))


if __name__ == "__main__":
    main()
