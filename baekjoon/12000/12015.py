from bisect import bisect_left


def get_lis_length(a: list[int]) -> int:
    cache: list[int] = []

    for num in a:
        if len(cache) == 0 or cache[-1] < num:
            cache.append(num)
        else:
            cache[bisect_left(cache, num)] = num

    return len(cache)


def main() -> None:
    _ = int(input())
    a = list(map(int, input().split()))

    print(get_lis_length(a))


if __name__ == "__main__":
    main()
