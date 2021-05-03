board: list[list[int]]
cache_row: list[list[bool]] = [[True] * 10 for _ in range(9)]
cache_col: list[list[bool]] = [[True] * 10 for _ in range(9)]
cache_square: list[list[bool]] = [[True] * 10 for _ in range(9)]


def get_square_position(ridx: int, cidx: int) -> int:
    return 3 * (ridx // 3) + cidx // 3


def init_caches() -> None:
    global cache_row, cache_col, cache_square
    for ridx in range(9):
        for cidx in range(9):
            num: int = board[ridx][cidx]
            if num != 0:
                cache_row[ridx][num] = False
                cache_col[cidx][num] = False
                cache_square[get_square_position(ridx, cidx)][num] = False


def solve_sudoku(position: int) -> bool:
    global board
    if position == 81:
        return True

    ridx: int = position // 9
    cidx: int = position % 9
    sidx: int = get_square_position(ridx, cidx)

    if board[ridx][cidx] != 0:
        return solve_sudoku(position + 1)

    for num in range(1, 10):
        if cache_row[ridx][num] and cache_col[cidx][num] and cache_square[sidx][num]:
            board[ridx][cidx] = num
            cache_row[ridx][num] = False
            cache_col[cidx][num] = False
            cache_square[sidx][num] = False

            if solve_sudoku(position + 1):
                return True

            board[ridx][cidx] = 0
            cache_row[ridx][num] = True
            cache_col[cidx][num] = True
            cache_square[sidx][num] = True

    return False


def main() -> None:
    global board
    board = [list(map(int, input())) for _ in range(9)]

    init_caches()
    solve_sudoku(0)
    for row in board:
        print(''.join(map(str, row)))


if __name__ == "__main__":
    main()
