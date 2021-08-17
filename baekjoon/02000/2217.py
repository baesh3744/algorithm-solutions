import sys


input = sys.stdin.readline


def main() -> None:
    n = int(input())
    rope_list = sorted(int(input()) for _ in range(n))

    max_weight: int = 0
    for index, rope in enumerate(rope_list):
        max_weight = max(max_weight, rope * (n - index))
    print(max_weight)


if __name__ == "__main__":
    main()
