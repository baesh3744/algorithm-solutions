def get_max_worth(n: int, m: int, board: list[list[int]]) -> int:
    cache = [[0 for _ in range(m)] for _ in range(n)]

    cache[0][0] = board[0][0]
    for cidx in range(1, m):
        cache[0][cidx] += board[0][cidx] + cache[0][cidx - 1]

    for ridx in range(1, n):
        left_cache: list[int] = [0 for _ in range(m)]
        left_cache[0] = cache[ridx - 1][0] + board[ridx][0]
        for cidx in range(1, m):
            left_cache[cidx] = max(left_cache[cidx - 1],
                                   cache[ridx - 1][cidx]) + board[ridx][cidx]

        right_cache: list[int] = [0 for _ in range(m)]
        right_cache[m - 1] = cache[ridx - 1][m - 1] + board[ridx][m - 1]
        for cidx in range(m - 2, -1, -1):
            right_cache[cidx] = max(right_cache[cidx + 1],
                                    cache[ridx - 1][cidx]) + board[ridx][cidx]

        for cidx in range(m):
            cache[ridx][cidx] = max(left_cache[cidx], right_cache[cidx])

    return cache[n - 1][m - 1]


def main() -> None:
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(get_max_worth(n, m, board))


if __name__ == "__main__":
    main()
