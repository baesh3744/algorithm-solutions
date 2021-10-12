def factorize(n: int) -> set[int]:
    factor_list: set[int] = set([])
    num: int = 2
    while num ** 2 <= n:
        while n % num == 0:
            factor_list.add(num)
            n //= num
        num += 1
    if n != 1:
        factor_list.add(n)
    return factor_list


def main() -> None:
    n = int(input())

    factor_list = factorize(n)
    cnt: float = float(n)
    for factor in factor_list:
        cnt *= (1 - 1 / factor)
    print(int(cnt))


if __name__ == "__main__":
    main()
