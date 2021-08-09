import sys
from typing import List


Board = List[List[int]]


def move(turn: int, is_collapsed_prev: bool, board: Board) -> int:
    if turn == 10:
        max_: int = 0
        for row in board:
            index, length = 0, len(row)
            while index < length:
                if index + 1 < length and row[index] == row[index + 1]:
                    max_ = max(max_, 2 * row[index])
                    index += 2
                else:
                    max_ = max(max_, row[index])
                    index += 1
        return max_

    max_: int = 0
    is_collapsed: bool = False
    board_right: Board = [[] for _ in range(n)]
    board_right_transposed: Board = [[] for _ in range(n)]
    board_left_transposed: Board = [[] for _ in range(n)]

    for ridx, row in enumerate(board):
        board_right[ridx] = row.copy()
        row = board_right[ridx]
        index = len(row) - 1
        while 0 <= index:
            if 0 <= index - 1 and row[index] == row[index - 1]:
                row[index - 1] += row.pop(index)
                is_collapsed = True
                index -= 2
            else:
                index -= 1

        for index, elem in enumerate(row[::-1]):
            board_right_transposed[index].append(elem)
            max_ = max(max_, elem)

    if max_ == max_value:
        print(max_)
        sys.exit()

    if not is_collapsed:
        if not is_collapsed_prev:
            return move(turn + 1, is_collapsed, board_right_transposed)
        else:
            for row in board_right:
                for index, elem in enumerate(row):
                    board_left_transposed[index].append(elem)
            return max(
                move(turn + 1, is_collapsed, board_right_transposed),
                move(turn + 1, is_collapsed, board_left_transposed),
            )

    board_left: Board = [[] for _ in range(n)]
    for ridx, row in enumerate(board):
        board_left[ridx] = row.copy()
        row = board_left[ridx]
        index, length = 0, len(row)
        while index < length:
            if index + 1 < length and row[index] == row[index + 1]:
                row[index] += row.pop(index + 1)
                length -= 1
            index += 1

        for index, elem in enumerate(row):
            board_left_transposed[index].append(elem)

    return max(
        move(turn + 1, is_collapsed, board_right),
        move(turn + 1, is_collapsed, board_left),
        move(turn + 1, is_collapsed, board_right_transposed),
        move(turn + 1, is_collapsed, board_left_transposed),
    )


def main() -> None:
    global n, max_value
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    lr_board = [list(filter(lambda x: x != 0, row)) for row in board]
    tb_board = [list(filter(lambda x: x != 0, col)) for col in zip(*board)]

    total = sum(map(lambda x: sum(x), lr_board))
    max_value = 1
    while total != 1:
        total //= 2
        max_value *= 2

    print(max(move(1, True, lr_board), move(1, True, tb_board)))


if __name__ == "__main__":
    main()
