import sys


EXPLOSIVE_RANGE = [(-1, 0), (0, -1), (0, 0), (0, 1), (1, 0)]

input = sys.stdin.readline


def get_all_bomb_board() -> list[list[str]]:
    return [["O" for _ in range(c)] for _ in range(r)]


def get_explosive_range(ridx: int, cidx: int) -> list[tuple[int, int]]:
    erange: list[tuple[int, int]] = []
    for move_ridx, move_cidx in EXPLOSIVE_RANGE:
        adj_ridx, adj_cidx = ridx + move_ridx, cidx + move_cidx
        if 0 <= adj_ridx < r and 0 <= adj_cidx < c:
            erange.append((adj_ridx, adj_cidx))
    return erange


def get_exploded_board(board: list[list[str]]) -> list[list[str]]:
    exploded_board: list[list[str]] = get_all_bomb_board()
    for ridx, row in enumerate(board):
        for cidx, elem in enumerate(row):
            if elem == "O":
                for adj_ridx, adj_cidx in get_explosive_range(ridx, cidx):
                    exploded_board[adj_ridx][adj_cidx] = "."
    return exploded_board


def print_board(board: list[list[str]]) -> None:
    for ridx in range(r):
        print("".join(board[ridx]))


if __name__ == "__main__":
    r, c, n = map(int, input().split())
    initial_board = [list(input().strip()) for _ in range(r)]

    if n == 1:
        print_board(initial_board)
    elif n % 2 == 0:
        print_board(get_all_bomb_board())
    elif n % 4 == 1:
        prev_board = get_exploded_board(initial_board)
        print_board(get_exploded_board(prev_board))
    else:
        print_board(get_exploded_board(initial_board))
