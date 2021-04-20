from typing import List, Tuple


tp: List[Tuple[int, ...]]
cache: List[int]


def get_max_money(cur: int) -> int:
    if cur == 0:
        return 0
    if cache[cur] != -1:
        return cache[cur]

    max_money: int = 0
    for next in range(cur - 1, -1, -1):
        if tp[next][0] + next <= cur:
            max_money = max(max_money, get_max_money(next) + tp[next][1])
    cache[cur] = max_money
    return max_money


def main() -> None:
    global tp, cache
    N = int(input())
    tp = [tuple(map(int, input().split())) for _ in range(N)]
    cache = [-1 for _ in range(N + 1)]

    print(get_max_money(N))


if __name__ == "__main__":
    main()
