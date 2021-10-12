import sys


MAX: int = sys.maxsize

input = sys.stdin.readline

# cache[section][type]
#   0   section의 위, 아래 모두 채운 상태
#   1   section의 위만 채운 상태
#   2   section의 아래만 채운 상태
def count(
    n: int, w: int, onetagon: list[list[int]], cache: list[list[int]]
) -> list[list[int]]:
    for section in range(2, n + 1):
        up: int = 1 if onetagon[0][section - 1] + onetagon[0][section] <= w else 2
        down: int = 1 if onetagon[1][section - 1] + onetagon[1][section] <= w else 2
        ver: int = 1 if onetagon[0][section] + onetagon[1][section] <= w else 2

        cache[0][section] = min(
            cache[0][section - 1] + ver,
            cache[0][section - 2] + up + down,
            cache[1][section - 1] + down + 1,
            cache[2][section - 1] + up + 1,
        )
        cache[1][section] = min(cache[2][section - 1] + up, cache[0][section - 1] + 1)
        cache[2][section] = min(cache[1][section - 1] + down, cache[0][section - 1] + 1)
    return cache


def solve(n: int, w: int, onetagon: list[list[int]]) -> int:
    ans: int = MAX
    cache = [[0 for _ in range(n + 1)] for _ in range(3)]

    up: int = onetagon[0][1]
    down: int = onetagon[1][1]

    can_combine_up: bool = onetagon[0][1] + onetagon[0][n] <= w
    can_combine_down: bool = onetagon[1][1] + onetagon[1][n] <= w

    cache[0][1] = 1 if onetagon[0][1] + onetagon[1][1] <= w else 2
    cache[1][1] = cache[2][1] = 1
    cache = count(n, w, onetagon, cache)
    ans = min(ans, cache[0][n])

    if can_combine_up:
        cache[0][1] = 2
        cache[1][1] = cache[2][1] = 1
        onetagon[0][1] = MAX
        cache = count(n, w, onetagon, cache)
        ans = min(ans, cache[2][n])
        onetagon[0][1] = up

    if can_combine_down:
        cache[0][1] = 2
        cache[1][1] = 1
        cache[2][1] = 1
        onetagon[1][1] = MAX
        cache = count(n, w, onetagon, cache)
        ans = min(ans, cache[1][n])
        onetagon[1][1] = down

    if can_combine_up and can_combine_down:
        cache[0][1] = 2
        cache[1][1] = cache[2][1] = 1
        onetagon[0][1] = onetagon[1][1] = MAX
        cache = count(n, w, onetagon, cache)
        ans = min(ans, cache[0][n - 1])

    return ans


def main() -> None:
    t = int(input())
    for _ in range(t):
        n, w = map(int, input().split())
        onetagon = [[-1] + list(map(int, input().split())) for _ in range(2)]
        if n == 1:
            print(1 if onetagon[0][1] + onetagon[1][1] <= w else 2)
        else:
            print(solve(n, w, onetagon))


if __name__ == "__main__":
    main()

# Reference https://kibbomi.tistory.com/128
