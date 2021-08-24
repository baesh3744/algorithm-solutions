MOD: int = 1000000007


def get_cache(n: int) -> list[list[int]]:
    cache: list[list[int]] = [[height for _ in range(2)] for height in range(n + 1)]
    for height in range(2, n + 1):
        # from root
        cache[height][0] = cache[height - 1][0] + cache[height - 1][1]
        # from leaf
        cache[height][1] = cache[height - 1][0]
        for sub_height in range(1, height - 1):
            cache[height][1] += cache[sub_height][1]
    return cache


def count_teleport(n: int, k: int) -> int:
    cache = get_cache(n)
    k_height = n - k + 1

    ans: int = 0
    if k_height == n:
        ans = cache[n][0]
    elif k_height == 1:
        ans = cache[n][1]
    else:
        ans += cache[n - 1][0]
        for height in range(k_height, n - 1):
            ans += cache[height][1]
        ans += 2 * cache[k_height - 1][1]
    return ans - 1


def main() -> None:
    n, k = map(int, input().split())

    print(count_teleport(n, k) % MOD)


if __name__ == "__main__":
    main()
