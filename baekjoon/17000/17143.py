import sys


Board = list[list[tuple[int, int, int]]]


def catch_shark(r: int, loc: int, board: Board) -> int:
    for row in range(1, r + 1):
        if len(board[row][loc]) != 0:
            return row
    return -1


def move_shark(bound: int, loc: int, speed: int, dir: int) -> tuple[int, int]:
    changed: list[int] = [0, 2, 1, 4, 3]
    is_changed: bool = False

    if dir == 1 or dir == 4:
        next_loc = loc - speed
    else:
        next_loc = loc + speed

    while next_loc < 1 or next_loc > bound:
        is_changed = not is_changed
        if next_loc < 1:
            next_loc = 2 - next_loc
        elif next_loc > bound:
            next_loc = 2 * bound - next_loc

    next_dir = changed[dir] if is_changed else dir

    return next_loc, next_dir


def update_board(r: int, c: int, board: Board) -> Board:
    new_board: Board = [[tuple() for _ in range(c + 1)] for _ in range(r + 1)]

    for row in range(1, r + 1):
        for col in range(1, c + 1):
            if len(board[row][col]) != 0:
                speed, dir, size = board[row][col]
                next_row, next_col, next_dir = row, col, dir

                if dir == 1 or dir == 2:
                    next_row, next_dir = move_shark(r, row, speed, dir)
                else:
                    next_col, next_dir = move_shark(c, col, speed, dir)

                if (len(new_board[next_row][next_col]) == 0 or
                        new_board[next_row][next_col][2] < size):
                    new_board[next_row][next_col] = (speed, next_dir, size)

    return new_board


def sum_caught_shark(r: int, c: int, loc: int, board: Board) -> int:
    if c < loc:
        return 0

    shark: int = 0

    row = catch_shark(r, loc, board)
    if row != -1:
        shark += board[row][loc][2]
        board[row][loc] = tuple()

    board = update_board(r, c, board)

    return shark + sum_caught_shark(r, c, loc + 1, board)


def main() -> None:
    r, c, m = map(int, input().split())
    board: Board = [[tuple() for _ in range(c + 1)] for _ in range(r + 1)]
    for _ in range(m):
        x, y, s, d, z = map(int, sys.stdin.readline().split())
        mod = 2 * (r - 1) if (d == 1 or d == 2) else 2 * (c - 1)
        if len(board[x][y]) == 0 or board[x][y][2] < z:
            board[x][y] = (s % mod, d, z)

    print(sum_caught_shark(r, c, 1, board))


if __name__ == "__main__":
    main()
