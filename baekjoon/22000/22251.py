LIGHT_LIST: list[list[bool]] = [
    [True, True, True, False, True, True, True],  # 0
    [False, False, True, False, False, True, False],  # 1
    [True, False, True, True, True, False, True],  # 2
    [True, False, True, True, False, True, True],  # 3
    [False, True, True, True, False, True, False],  # 4
    [True, True, False, True, False, True, True],  # 5
    [True, True, False, True, True, True, True],  # 6
    [True, False, True, False, False, True, False],  # 7
    [True, True, True, True, True, True, True],  # 8
    [True, True, True, True, False, True, True],  # 9
]


def make_diff_table() -> None:
    global diff_table
    diff_table = [[0 for _ in range(10)] for _ in range(10)]
    for fnum in range(10):
        for snum in range(fnum + 1, 10):
            diff = sum(
                1
                for first, second in zip(LIGHT_LIST[fnum], LIGHT_LIST[snum])
                if first != second
            )
            diff_table[fnum][snum] = diff
            diff_table[snum][fnum] = diff


def count_diff(k: int, num: int, x: int) -> int:
    diff: int = 0
    for _ in range(k):
        diff += diff_table[num % 10][x % 10]
        num, x = num // 10, x // 10
    return diff


def main() -> None:
    n, k, p, x = map(int, input().split())

    make_diff_table()

    ans: int = 0
    for num in range(1, n + 1):
        if 1 <= count_diff(k, num, x) <= p:
            ans += 1
    print(ans)


if __name__ == "__main__":
    main()
