import bisect


def get_lis_length(values: list[int]) -> int:
    lis: list[int] = []
    for value in values:
        if not lis or lis[-1] < value:
            lis.append(value)
        else:
            lis[bisect.bisect_left(lis, value)] = value
    return len(lis)


def main() -> None:
    while True:
        try:
            _ = int(input())
            values = list(map(int, input().split()))
            print(get_lis_length(values))
        except Exception:
            break


if __name__ == "__main__":
    main()
