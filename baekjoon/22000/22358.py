import sys
from typing import List, Tuple


MAX: int = sys.maxsize

input = sys.stdin.readline

ski_list: List[List[Tuple[int, int]]]
lift_list: List[List[int]]


def dp(n: int, k: int, s: int, t: int) -> int:
    cache = [[-1 * MAX for _ in range(11)] for _ in range(n + 1)]
    for lift in range(k + 1):
        cache[t][lift] = 0
        for station in range(n, 0, -1):
            for _upper, _time in ski_list[station]:
                cache[station][lift] = max(
                    cache[station][lift], cache[_upper][lift] + _time
                )
            if lift == 0:
                continue
            for _lower in lift_list[station]:
                cache[station][lift] = max(
                    cache[station][lift], cache[_lower][lift - 1]
                )
    return max(-1, cache[s][k])


def main() -> None:
    global ski_list, lift_list
    n, m, k, s, t = map(int, input().split())

    ski_list = [[] for _ in range(n + 1)]
    lift_list = [[] for _ in range(n + 1)]
    for _ in range(m):
        ai, bi, ti = map(int, input().split())
        ski_list[ai].append((bi, ti))
        lift_list[bi].append(ai)

    print(dp(n, k, s, t))


if __name__ == "__main__":
    sys.setrecursionlimit(200000)
    main()

# reference "jeongdongha" https://www.acmicpc.net/source/31830389
