def initialize_cache(N: int) -> None:
    global cache
    cache = [1000000 for _ in range(N + 1)]

    cache[0] = -1
    cache[1] = 0
    for num in range(2, N + 1):
        if num % 3 == 0:
            cache[num] = min(cache[num], cache[num // 3] + 1)  # 1
        if num % 2 == 0:
            cache[num] = min(cache[num], cache[num // 2] + 1)  # 2
        cache[num] = min(cache[num], cache[num - 1] + 1)  # 3


def print_order(N: int) -> None:
    print(cache[N])

    num: int = N
    while num > 0:
        print(num, end=" ")

        if num % 3 == 0 and cache[num] == cache[num // 3] + 1:
            num //= 3
        elif num % 2 == 0 and cache[num] == cache[num // 2] + 1:
            num //= 2
        else:
            num -= 1
    print()


def main() -> None:
    N = int(input())

    initialize_cache(N)
    print_order(N)


if __name__ == "__main__":
    main()
