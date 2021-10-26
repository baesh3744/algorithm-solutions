import sys
from collections import deque
from itertools import product


MOVE_LIST = [(-1, 0), (0, 1), (1, 0), (0, -1)]
PLANAR_FIGURES = [
    set([(0, 0), (1, 0), (2, 0), (1, 1), (1, 2), (1, 3)]),
    set([(0, 0), (1, 0), (0, 1), (-1, 1), (0, 2), (0, 3)]),
    set([(0, 0), (1, 0), (0, 1), (0, 2), (-1, 2), (0, 3)]),
    set([(0, 0), (1, 0), (0, 1), (0, 2), (0, 3), (-1, 3)]),
    set([(0, 0), (0, 1), (-1, 1), (1, 1), (0, 2), (0, 3)]),
    set([(0, 0), (0, 1), (1, 1), (0, 2), (-1, 2), (0, 3)]),
    set([(0, 0), (0, 1), (0, 2), (-1, 2), (-1, 3), (-1, 4)]),
    set([(0, 0), (0, 1), (-1, 1), (-1, 2), (-2, 2), (-2, 3)]),
    set([(0, 0), (-1, 0), (-1, 1), (-1, 2), (-2, 2), (-2, 3)]),
    set([(0, 0), (0, 1), (1, 1), (2, 1), (1, 2), (1, 3)]),
    set([(0, 0), (0, 1), (-1, 1), (0, 2), (1, 2), (1, 3)]),
]

input = sys.stdin.readline


def get_figure(board: list[list[int]], ridx: int, cidx: int) -> set[tuple[int, int]]:
    figure: set[tuple[int, int]] = set()
    que: deque[tuple[int, int]] = deque()

    que.append((ridx, cidx))
    figure.add((0, 0))

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in MOVE_LIST:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if (
                0 <= next_ridx < 6
                and 0 <= next_cidx < 6
                and board[next_ridx][next_cidx] == 1
                and (next_ridx - ridx, next_cidx - cidx) not in figure
            ):
                que.append((next_ridx, next_cidx))
                figure.add((next_ridx - ridx, next_cidx - cidx))

    return figure


def turn_figure(figure: set[tuple[int, int]]) -> list[set[tuple[int, int]]]:
    figures = [figure]
    figures += [set((-ridx, cidx) for ridx, cidx in fig) for fig in figures]
    figures += [set((ridx, -cidx) for ridx, cidx in fig) for fig in figures]
    figures += [set((cidx, ridx) for ridx, cidx in fig) for fig in figures]
    return figures


def is_same(figures: list[set[tuple[int, int]]]) -> bool:
    for my, correct in product(figures, PLANAR_FIGURES):
        if my == correct:
            return True
    return False


def is_planar_figure_of_cube(board: list[list[int]]) -> bool:
    for ridx, row in enumerate(board):
        for cidx, elem in enumerate(row):
            if elem == 0:
                continue
            figure = get_figure(board, ridx, cidx)
            figures = turn_figure(figure)
            if is_same(figures):
                return True
    return False


def main() -> None:
    for _ in range(3):
        board = [list(map(int, input().split())) for _ in range(6)]
        print("yes" if is_planar_figure_of_cube(board) else "no")


if __name__ == "__main__":
    main()
