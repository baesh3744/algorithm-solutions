MOD: int = 1000000007


def main() -> None:
    n, k = map(int, input().split())

    cnt: int = 0
    for height in range(3, n + 1):
        cnt = 2 * cnt + 2 * (height % 2)
    print((cnt + (n + k) % 2) % MOD)


if __name__ == "__main__":
    main()
