from typing import Final


MOD: Final[int] = 1000000000


def dp(N: int, K: int) -> int:
    if K == 1:
        return 1
    if cache[N][K] != -1:
        return cache[N][K]

    ret: int = 0
    for num in range(N + 1):
        ret += dp(N - num, K - 1)
    cache[N][K] = ret % MOD
    return cache[N][K]


def main() -> None:
    global cache
    N, K = map(int, input().split())

    cache = [[-1 for _ in range(K + 1)] for _ in range(N + 1)]

    print(dp(N, K))


if __name__ == "__main__":
    main()
