def count_prime_number(n: int, pnumber: int) -> int:
    cnt, divider = 0, pnumber
    while divider <= n:
        cnt += n // divider
        divider *= pnumber
    return cnt


def main() -> None:
    n = int(input())

    print(count_prime_number(n, 5))


if __name__ == "__main__":
    main()
