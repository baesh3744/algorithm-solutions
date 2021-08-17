MOD: int = 1000000007


def list_building(total: int, left: int, right: int) -> int:
    if total == 1 or (left == 1 and right == 1):
        return 1 if total + left + right == 3 else 0
    if cache[total][left][right] != -1:
        return cache[total][left][right]

    ans: int = 0
    ans += (total - 2) * list_building(total - 1, left, right)
    if left - 1 >= 1:
        ans += list_building(total - 1, left - 1, right)
    if right - 1 >= 1:
        ans += list_building(total - 1, left, right - 1)
    cache[total][left][right] = ans % MOD
    return cache[total][left][right]


def main() -> None:
    global n, l, r, cache
    n, l, r = map(int, input().split())

    cache = [[[-1 for _ in range(n + 1)] for _ in range(n + 1)] for _ in range(n + 1)]
    print(list_building(n, l, r))


if __name__ == "__main__":
    main()
