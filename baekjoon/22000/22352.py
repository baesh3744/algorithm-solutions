import sys
from collections import deque


YES: str = "YES"
NO: str = "NO"
MOVE_LIST: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

Board = list[list[int]]

input = sys.stdin.readline


def spread(ridx: int, cidx: int, to_value: int, origin_board: Board) -> Board:
    from_value: int = origin_board[ridx][cidx]
    que: deque[tuple[int, int]] = deque()

    que.append((ridx, cidx))
    origin_board[ridx][cidx] = to_value

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in MOVE_LIST:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if (
                0 <= next_ridx < n
                and 0 <= next_cidx < m
                and origin_board[next_ridx][next_cidx] == from_value
            ):
                que.append((next_ridx, next_cidx))
                origin_board[next_ridx][next_cidx] = to_value

    return origin_board


def check(origin_board: Board, result_board: Board) -> str:
    for ridx in range(n):
        for cidx in range(m):
            if origin_board[ridx][cidx] != result_board[ridx][cidx]:
                return NO
    return YES


def compare(origin_board: Board, result_board: Board) -> str:
    for ridx in range(n):
        for cidx in range(m):
            if origin_board[ridx][cidx] != result_board[ridx][cidx]:
                origin_board = spread(
                    ridx, cidx, result_board[ridx][cidx], origin_board
                )
                return check(origin_board, result_board)
    return YES


def main() -> None:
    global n, m
    n, m = map(int, input().split())
    origin_board = [list(map(int, input().split())) for _ in range(n)]
    result_board = [list(map(int, input().split())) for _ in range(n)]

    print(compare(origin_board, result_board))


if __name__ == "__main__":
    main()
