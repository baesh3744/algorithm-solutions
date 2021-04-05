from typing import Final


MOD: Final[int] = 1000000000
ALL_USED: Final[int] = (1 << 10) - 1


def solve(N: int, last: int, length: int, used: int) -> int:
    if length == N:
        return 1 if used == ALL_USED else 0
    if cache[last][length][used] != -1:
        return cache[last][length][used]

    count: int = 0
    for next in [last - 1, last + 1]:
        if 0 <= next <= 9:
            count += solve(N, next, length + 1, used | 1 << next)

    cache[last][length][used] = count % MOD
    return cache[last][length][used]


def main() -> None:
    global cache
    N = int(input())

    count: int = 0
    for num in range(1, 10):
        cache = [[[-1 for _ in range(1 << 10)]
                  for _ in range(N)] for _ in range(10)]
        used: int = 1 << num
        count += solve(N, num, 1, used)
    print(count % MOD)


if __name__ == "__main__":
    main()
