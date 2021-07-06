import itertools
import sys


Board = list[list[int]]


def make_section_board(n: int, x: int, y: int, d1: int, d2: int) -> Board:
    board: Board = [[0 for _ in range(n)] for _ in range(n)]

    for d in range(d1 + 1):
        board[x + d - 1][y - d - 1] = 5
        board[x + d2 + d - 1][y + d2 - d - 1] = 5
    for d in range(d2 + 1):
        board[x + d - 1][y + d - 1] = 5
        board[x + d1 + d - 1][y - d1 + d - 1] = 5

    for ridx in range(1, n + 1):
        is_section5 = False
        for cidx in range(1, n + 1):
            if ((ridx == x and cidx == y) or
                    (ridx == x + d1 + d2 and cidx == y - d1 + d2)):
                continue
            if board[ridx - 1][cidx - 1] == 5:
                is_section5 = not is_section5
            elif is_section5:
                board[ridx - 1][cidx - 1] = 5
            elif ridx < x + d1 and cidx <= y:
                board[ridx - 1][cidx - 1] = 1
            elif ridx <= x + d2 and y < cidx <= n:
                board[ridx - 1][cidx - 1] = 2
            elif x + d1 <= ridx <= n and cidx < y - d1 + d2:
                board[ridx - 1][cidx - 1] = 3
            else:
                board[ridx - 1][cidx - 1] = 4

    return board


def get_min_population_diff(n: int, city: Board, section_board: Board) -> int:
    populations = [0] * 5
    for ridx in range(n):
        for cidx in range(n):
            populations[section_board[ridx][cidx] - 1] += city[ridx][cidx]
    return max(populations) - min(populations)


def split_fair_section(n: int, city: Board) -> int:
    min_diff = sys.maxsize

    for x, y, d1, d2 in itertools.product(range(1, n + 1), repeat=4):
        if not (x + d1 + d2 <= n and 1 <= y - d1 and y + d2 <= n):
            continue

        section_board = make_section_board(n, x, y, d1, d2)
        min_diff = min(min_diff,
                       get_min_population_diff(n, city, section_board))

    return min_diff


def main() -> None:
    n = int(input())
    city = [list(map(int, input().split())) for _ in range(n)]

    print(split_fair_section(n, city))


if __name__ == "__main__":
    main()
