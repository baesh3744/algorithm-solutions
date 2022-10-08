from copy import deepcopy
import sys


input = sys.stdin.readline


def append_zeros(n: int, board: list[list[int]]) -> list[list[int]]:
    appended = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    for row in range(1, n + 1):
        for column in range(1, n + 1):
            appended[row][column] = board[row - 1][column - 1]

    return appended


def accumulate_board(n: int, board: list[list[int]]) -> list[list[int]]:
    accumulated = deepcopy(board)

    for row in range(n + 1):
        for column in range(n + 1):
            if column - 1 >= 0:
                accumulated[row][column] += accumulated[row][column - 1]

    for column in range(n + 1):
        for row in range(n + 1):
            if row - 1 >= 0:
                accumulated[row][column] += accumulated[row - 1][column]

    return accumulated


def main() -> None:
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    board_with_zeros = append_zeros(n, board)
    accumulated = accumulate_board(n, board_with_zeros)

    for _ in range(m):
        x1, y1, x2, y2 = map(int, input().split())
        print(
            accumulated[x2][y2]
            - accumulated[x2][y1 - 1]
            - accumulated[x1 - 1][y2]
            + accumulated[x1 - 1][y1 - 1]
        )


if __name__ == "__main__":
    main()
