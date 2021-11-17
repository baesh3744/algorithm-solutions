from math import comb


MOD = 1000000


def count(n: int) -> int:
    if n == 1:
        return 1

    cache = [0 for _ in range(n + 1)]

    cache[0] = cache[1] = 1
    for i in range(2, n + 1):
        for k in range(i):
            cache[i] += comb(i - 1, k) * cache[k] * cache[i - k - 1]
        cache[i] = cache[i] // 2 % MOD

    return cache[n] * 2 % MOD


if __name__ == "__main__":
    n = int(input())

    print(count(n))
