import math


def main() -> None:
    N, K = map(int, input().split())
    _ = list(map(int, input().split()))

    print(math.ceil((N - 1) / (K - 1)))


if __name__ == "__main__":
    main()
