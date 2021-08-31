def count(num: int, prime: int) -> int:
    cnt: int = 0
    while 0 < num:
        cnt += num // prime
        num //= prime
    return cnt


def main() -> None:
    n, m = map(int, input().split())

    cnt = min(
        count(n, 5) - count(m, 5) - count(n - m, 5),
        count(n, 2) - count(m, 2) - count(n - m, 2),
    )
    print(cnt if cnt >= 0 else 0)


if __name__ == "__main__":
    main()
