from typing import List


MOVE: List[List[int]] = [[-1, 0], [0, -1]]


def is_range(row: int, col: int) -> bool:
    return 0 <= row and row < M and 0 <= col and col < N


def get_max_clothes(row: int, col: int) -> int:
    if row == 0 and col == 0:
        return clothes[row][col]
    if cache[row][col] != -1:
        return cache[row][col]

    max_clothes: int = 0
    for move_row, move_col in MOVE:
        next_row: int = row + move_row
        next_col: int = col + move_col
        if is_range(next_row, next_col):
            max_clothes = max(max_clothes, get_max_clothes(
                next_row, next_col) + clothes[row][col])
    cache[row][col] = max_clothes
    return max_clothes


def main() -> None:
    global N, M, clothes, cache
    N, M = map(int, input().split())
    clothes = [list(map(int, input().split())) for _ in range(M)]

    cache = [[-1 for _ in range(N)] for _ in range(M)]

    print(get_max_clothes(M - 1, N - 1))


if __name__ == "__main__":
    main()
