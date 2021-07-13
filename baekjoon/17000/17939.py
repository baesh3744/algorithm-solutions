def get_max_profit(chart: list[int]) -> int:
    if not chart:
        return 0

    max_value = max(chart)
    sell_idx = chart.index(max_value)
    profit: int = 0
    for value in chart[:sell_idx]:
        profit += max_value - value
    return profit + get_max_profit(chart[sell_idx + 1:])


def main() -> None:
    _ = int(input())
    chart = list(map(int, input().split()))
    print(get_max_profit(chart))


if __name__ == "__main__":
    main()
