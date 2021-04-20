from typing import List


def get_stair_counts(row: List[int]) -> List[List[int]]:
    stair_counts: List[List[int]] = []
    for item in row:
        if len(stair_counts) == 0 or stair_counts[-1][0] != item:
            stair_counts.append([item, 1])
        else:
            stair_counts[-1][1] += 1
    return stair_counts


def is_passable_row(l: int, row: List[int]) -> bool:
    stair_counts: List[List[int]] = get_stair_counts(row)

    be_deleted: int = -1
    for idx in range(len(stair_counts) - 1):
        cur_stair: int = stair_counts[idx][0]
        next_stair: int = stair_counts[idx + 1][0]
        if cur_stair == next_stair - 1:
            be_deleted = idx
        elif cur_stair == next_stair + 1:
            be_deleted = idx + 1
        else:
            return False

        stair_counts[be_deleted][1] -= l

        if stair_counts[be_deleted][1] < 0:
            return False

    return True


def count_passable_rows(l: int, board: List[List[int]]) -> int:
    prow_count: int = 0
    for row in board:
        if is_passable_row(l, row):
            prow_count += 1
    return prow_count


def turn_board(n: int, board: List[List[int]]) -> List[List[int]]:
    turned_board: List[List[int]] = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            turned_board[i][j] = board[j][i]
    return turned_board


def main() -> None:
    n, l = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ans: int = 0
    ans += count_passable_rows(l, board)
    ans += count_passable_rows(l, turn_board(n, board))
    print(ans)


if __name__ == "__main__":
    main()
