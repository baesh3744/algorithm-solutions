import sys
from itertools import permutations


input = sys.stdin.readline


def main() -> None:
    _, m = map(int, input().split())
    numbers = map(int, input().split())

    for combination in permutations(sorted(numbers), m):
        print(" ".join(map(str, combination)))


if __name__ == "__main__":
    main()
