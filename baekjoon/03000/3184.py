from typing import Final, List, Tuple
from queue import Queue


MOVE: Final[List[Tuple[int, int]]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
que: "Queue[Tuple[int, int]]" = Queue()


def is_range(row: int, col: int) -> bool:
    return 0 <= row < R and 0 <= col < C


def insert_que(ridx: int, cidx: int, sheep: int, wolf: int) -> Tuple[int, int]:
    if yard[ridx][cidx] == 'o':
        sheep += 1
    elif yard[ridx][cidx] == 'v':
        wolf += 1
    yard[ridx][cidx] = '#'
    que.put((ridx, cidx))
    return sheep, wolf


def count_alive(ridx: int, cidx: int) -> Tuple[int, int]:
    sheep: int = 0
    wolf: int = 0

    sheep, wolf = insert_que(ridx, cidx, sheep, wolf)
    while not que.empty():
        row, col = que.get()
        for move_row, move_col in MOVE:
            next_row: int = row + move_row
            next_col: int = col + move_col

            if not is_range(next_row, next_col) or yard[next_row][next_col] == '#':
                continue

            sheep, wolf = insert_que(next_row, next_col, sheep, wolf)
    return sheep, wolf


def solve() -> Tuple[int, int]:
    total_sheep: int = 0
    total_wolf: int = 0
    for ridx, row in enumerate(yard):
        for cidx, item in enumerate(row):
            if item != '#':
                sheep, wolf = count_alive(ridx, cidx)
                if sheep > wolf:
                    total_sheep += sheep
                else:
                    total_wolf += wolf
    return total_sheep, total_wolf


def main() -> None:
    global R, C, yard
    R, C = map(int, input().split())
    yard = [[ch for ch in input()] for _ in range(R)]

    sheep, wolf = solve()
    print(sheep, wolf)


if __name__ == "__main__":
    main()
