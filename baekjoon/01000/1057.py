def get_power(num: int) -> int:
    power: int = 0
    while 2 ** power < num:
        power += 1
    return power


def get_round(jimin: int, hansu: int) -> int:
    j_power = get_power(jimin)
    h_power = get_power(hansu)

    if j_power == h_power:
        prev: int = 2 ** (j_power - 1)
        return get_round(jimin - prev, hansu - prev)
    return max(j_power, h_power)


def main() -> None:
    _, jimin, hansu = map(int, input().split())

    print(get_round(jimin, hansu))


if __name__ == "__main__":
    main()
