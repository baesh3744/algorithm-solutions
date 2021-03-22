from typing import List


def is_out_of_range(i: int, j: int) -> bool:
    return i < 0 or N <= i or j < 0 or M <= j


def add_values(i: int, j: int, move_i: List[int], move_j: List[int]) -> int:
    sum: int = 0
    for index in range(4):
        next_i: int = i + move_i[index]
        next_j: int = j + move_j[index]

        if is_out_of_range(next_i, next_j):
            return -1

        sum += board[next_i][next_j]
    return sum


def count_tetromino(i: int, j: int) -> int:
    default_move_i: List[List[int]] = [[0, 0, 0, 0], [0, 0, 1, 1],
                                       [0, 1, 2, 2], [0, 1, 1, 2], [0, 0, 0, 1]]
    default_move_j: List[List[int]] = [[0, 1, 2, 3], [0, 1, 0, 1],
                                       [0, 0, 0, 1], [0, 0, 1, 1], [0, 1, 2, 1]]

    max_sum: int = 0
    rotations: List[List[int]] = [[]]
    for index in range(5):
        if index == 0 or index == 1:
            rotations = [[1, 1]]
        elif index == 2:
            rotations = [[1, 1], [-1, 1], [1, -1], [-1, -1]]
        elif index == 3:
            rotations = [[1, 1], [1, -1]]
        else:
            rotations = [[1, 1], [-1, 1]]

        for rotation_i, rotation_j in rotations:
            move_i = [rotation_i * dmi for dmi in default_move_i[index]]
            move_j = [rotation_j * dmj for dmj in default_move_j[index]]

            max_sum = max(max_sum, add_values(i, j, move_i, move_j))
            max_sum = max(max_sum, add_values(i, j, move_j, move_i))

    return max_sum


def solve() -> None:
    ans: int = 0
    for i in range(N):
        for j in range(M):
            ans = max(ans, count_tetromino(i, j))
    print(ans)


def main() -> None:
    global N, M, board
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    solve()


if __name__ == "__main__":
    main()
