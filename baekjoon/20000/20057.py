import math
import sys


input = sys.stdin.readline

MOVE_RIDX: list[int] = [-1, 1, -2, -1, 1, 2, -1,  1,  0,  0]
MOVE_CIDX: list[int] = [1,  1,  0,  0, 0, 0, -1, -1, -2, -1]
MOVE_MINUS_CIDX: list[int] = [-1,  -1,  0,  0, 0, 0, 1, 1, 2, 1]
PERCENT: list[int] = [1, 1, 2, 7, 7, 2, 10, 10, 5]

n: int
board: list[list[int]]


def get_next(dir: int) -> tuple[list[int], list[int]]:
    if dir == 1:  # 좌
        return MOVE_RIDX, MOVE_CIDX
    elif dir == 2:  # 우
        return MOVE_RIDX, MOVE_MINUS_CIDX
    elif dir == 3:  # 상
        return MOVE_CIDX, MOVE_RIDX
    else:  # 하
        return MOVE_MINUS_CIDX, MOVE_RIDX


def get_spreaded(ridx: int, cidx: int) -> list[int]:
    sand = board[ridx][cidx]
    board[ridx][cidx] = 0

    spreaded = [math.floor(sand * percent / 100) for percent in PERCENT]
    spreaded.append(sand - sum(spreaded))
    return spreaded


def is_range(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < n and 0 <= cidx < n


def move_tornado(ridx: int, cidx: int, dir: int) -> int:
    if board[ridx][cidx] == 0:
        return 0

    out_of_range = 0
    for value in zip(*get_next(dir), get_spreaded(ridx, cidx)):
        move_ridx, move_cidx, spreaded = value
        next_ridx = ridx + move_ridx
        next_cidx = cidx + move_cidx
        if is_range(next_ridx, next_cidx):
            board[next_ridx][next_cidx] += spreaded
        else:
            out_of_range += spreaded
    return out_of_range


def get_out_of_range():
    out_of_range = 0
    start_ridx, start_cidx = n // 2, n // 2

    for turn in range(1, n//2 + 1):
        start_cidx -= 1
        out_of_range += move_tornado(start_ridx, start_cidx, 1)

        for _ in range(2*turn - 1):
            start_ridx += 1
            out_of_range += move_tornado(start_ridx, start_cidx, 4)

        for _ in range(2*turn):
            start_cidx += 1
            out_of_range += move_tornado(start_ridx, start_cidx, 2)

        for _ in range(2*turn):
            start_ridx -= 1
            out_of_range += move_tornado(start_ridx, start_cidx, 3)

        for _ in range(2*turn):
            start_cidx -= 1
            out_of_range += move_tornado(start_ridx, start_cidx, 1)

    return out_of_range


def main() -> None:
    global n, board
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    print(get_out_of_range())


if __name__ == "__main__":
    main()
