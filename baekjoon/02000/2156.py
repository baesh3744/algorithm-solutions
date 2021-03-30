from typing import List


def drink_max_wine(n: int) -> int:
    cache: List[List[int]] = [[0, 0, 0], [0, 0, 0]]

    for pos in range(1, n + 1):
        cur_idx: int = pos % 2
        pre_idx: int = (pos - 1) % 2

        cache[cur_idx][0] = max(cache[pre_idx])
        cache[cur_idx][1] = cache[pre_idx][0] + wines[pos - 1]
        cache[cur_idx][2] = cache[pre_idx][1] + wines[pos - 1]

    return max(cache[n % 2])


def main() -> None:
    global wines
    n = int(input())
    wines = [int(input()) for _ in range(n)]

    print(drink_max_wine(n))


if __name__ == "__main__":
    main()
