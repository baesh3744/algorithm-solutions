MOD = 1000000007


def main() -> None:
    n = int(input())

    cache = [0 for _ in range(n + 1)]
    cache[0] = 1
    for num in range(2, n + 1):
        cache[num] = ((num - 1) * (cache[num - 1] + cache[num - 2])) % MOD

    fac = 1
    for num in range(1, n + 1):
        fac = (fac * num) % MOD

    print(fac * cache[n] % MOD)


if __name__ == "__main__":
    main()
