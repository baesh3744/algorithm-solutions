from typing import List, Tuple


def count_cleaning(n: int,
                   m: int,
                   r: int,
                   c: int,
                   d: int,
                   board: List[List[int]]) -> int:
    cleaning: int = 0
    cur_ridx: int = r
    cur_cidx: int = c
    cur_dir: int = d
    has_cleaning: bool = True
    moves: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    while True:
        # 1
        if has_cleaning:
            board[cur_ridx][cur_cidx] = 2
            cleaning += 1

        # 2, 2-b
        has_cleaning = False
        for move in range(4):
            next_dir: int = cur_dir - move - 1
            if next_dir < 0:
                next_dir += 4
            next_ridx: int = cur_ridx + moves[next_dir][0]
            next_cidx: int = cur_cidx + moves[next_dir][1]

            # 2-a
            if (0 <= next_ridx < n and 0 <= next_cidx < m
                    and board[next_ridx][next_cidx] == 0):
                cur_ridx = next_ridx
                cur_cidx = next_cidx
                cur_dir = next_dir
                has_cleaning = True
                break

        if not has_cleaning:
            back_ridx: int = cur_ridx - moves[cur_dir][0]
            back_cidx: int = cur_cidx - moves[cur_dir][1]

            if board[back_ridx][back_cidx] != 1:  # 2-c
                cur_ridx = back_ridx
                cur_cidx = back_cidx
            else:  # 2-d
                break

    return cleaning


def main() -> None:
    n, m = map(int, input().split())
    r, c, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(count_cleaning(n, m, r, c, d, board))


if __name__ == "__main__":
    main()
