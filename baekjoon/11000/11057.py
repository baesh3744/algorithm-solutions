from typing import Final, List


MOD: Final[int] = 10007


def count_ascent_num(n: int) -> int:
    cache: List[List[int]] = [[1 for _ in range(10)] for _ in range(2)]

    for len in range(2, n + 1):
        for num in range(10):
            cache[len % 2][num] = sum(cache[(len - 1) % 2][:num + 1]) % MOD
    return sum(cache[n % 2]) % MOD


def main() -> None:
    N = int(input())

    print(count_ascent_num(N))


if __name__ == "__main__":
    main()
