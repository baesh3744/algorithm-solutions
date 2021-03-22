from typing import List


columns: List[bool]
add_diagonals: List[bool]
sub_diagonals: List[bool]


def initialize_board(N: int) -> None:
    global columns, add_diagonals, sub_diagonals
    columns = [False for _ in range(N)]
    add_diagonals = [False for _ in range(2 * N)]
    sub_diagonals = [False for _ in range(2 * N)]


def update_board(col: int, add: int, sub: int, value: bool) -> None:
    columns[col] = value
    add_diagonals[add] = value
    sub_diagonals[sub] = value


def solve(N: int, remains: int) -> int:
    if remains == 0:
        return 1

    ret: int = 0
    row_index: int = N - remains
    for col_index, col in enumerate(columns):
        add_index = row_index + col_index
        sub_index = row_index - col_index + N
        if col or add_diagonals[add_index] or sub_diagonals[sub_index]:
            continue

        update_board(col_index, add_index, sub_index, True)
        ret += solve(N, remains - 1)
        update_board(col_index, add_index, sub_index, False)
    return ret


def main() -> None:
    N = int(input())
    initialize_board(N)
    print(solve(N, N))


if __name__ == "__main__":
    main()
