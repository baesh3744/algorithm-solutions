import copy
from typing import Final, List


MAX: Final[int] = 6000


def calc_min_row_sum(A: List[List[int]]) -> int:
    min_sum: int = MAX
    for row in A:
        min_sum = min(min_sum, sum(row))
    return min_sum


def rotate_array(A: List[List[int]], cmd_idx: int) -> List[List[int]]:
    r, c, s = cmd[cmd_idx]
    rotated_A: List[List[int]] = copy.deepcopy(A)

    for idx in range(s):
        start_ridx: int = r - s - 1 + idx
        start_cidx: int = c - s - 1 + idx
        end_ridx: int = r + s - 1 - idx
        end_cidx: int = c + s - 1 - idx

        tmp: int = rotated_A[start_ridx][start_cidx]
        for ridx in range(start_ridx, end_ridx):
            rotated_A[ridx][start_cidx] = rotated_A[ridx + 1][start_cidx]

        for cidx in range(start_cidx, end_cidx):
            rotated_A[end_ridx][cidx] = rotated_A[end_ridx][cidx + 1]

        for ridx in range(end_ridx, start_ridx, -1):
            rotated_A[ridx][end_cidx] = rotated_A[ridx - 1][end_cidx]

        for cidx in range(end_cidx, start_cidx + 1, -1):
            rotated_A[start_ridx][cidx] = rotated_A[start_ridx][cidx - 1]
        rotated_A[start_ridx][start_cidx + 1] = tmp

    return rotated_A


def get_min_row_sum(A: List[List[int]], is_rotated: List[bool]) -> int:
    if all(is_rotated):
        return calc_min_row_sum(A)

    min_sum: int = MAX
    for idx, rotated in enumerate(is_rotated):
        if not rotated:
            is_rotated[idx] = True

            min_sum = min(min_sum,
                          get_min_row_sum(rotate_array(A, idx), is_rotated))

            is_rotated[idx] = False

    return min_sum


def main() -> None:
    global cmd
    N, _, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]
    cmd = [list(map(int, input().split())) for _ in range(K)]

    is_rotated: List[bool] = [False for _ in range(K)]
    print(get_min_row_sum(A, is_rotated))


if __name__ == "__main__":
    main()
