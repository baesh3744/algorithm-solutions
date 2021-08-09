def put_hive_oneside(n: int, honey: list[int]) -> int:
    excluded = honey[1] * 2
    min_excluded = excluded
    for index in range(2, n - 1):
        excluded += 2 * honey[index] - honey[index - 1]
        min_excluded = min(min_excluded, excluded)
    return 2 * sum(honey[1:]) - min_excluded


def put_hive_inside(honey: list[int]) -> int:
    sum_, max_ = 0, 0
    for hon in honey[1:-1]:
        sum_ += hon
        max_ = max(max_, hon)
    return sum_ + max_


def main() -> None:
    n = int(input())
    honey = list(map(int, input().split()))

    max_oneside = max(
        put_hive_oneside(n, honey), put_hive_oneside(n, list(reversed(honey)))
    )
    print(max(max_oneside, put_hive_inside(honey)))


if __name__ == "__main__":
    main()
