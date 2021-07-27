import sys
from collections import deque


Board = list[list[int]]
Point = tuple[int, int]

input = sys.stdin.readline

moves = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1),           (0, 1),
    (1, -1),  (1, 0),  (1, 1)
]


def remove_island(w: int, h: int, ridx: int, cidx: int, board: Board) -> Board:
    que: deque[Point] = deque()
    visited = [[False]*w for _ in range(h)]

    que.append((ridx, cidx))
    visited[ridx][cidx] = True
    board[ridx][cidx] = 0

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_x, move_y in moves:
            next_ridx = cur_ridx + move_x
            next_cidx = cur_cidx + move_y

            if 0 <= next_ridx < h and 0 <= next_cidx < w \
               and board[next_ridx][next_cidx] == 1:
                que.append((next_ridx, next_cidx))
                visited[next_ridx][next_cidx] = True
                board[next_ridx][next_cidx] = 0

    return board


def count_island(w: int, h: int, board: Board) -> int:
    cnt: int = 0
    for ridx, row in enumerate(board):
        for cidx, elem in enumerate(row):
            if elem == 1:
                board = remove_island(w, h, ridx, cidx, board)
                cnt += 1
    return cnt


def main() -> None:
    while True:
        w, h = map(int, input().split())
        if w == 0 and h == 0:
            break
        board = [list(map(int, input().split())) for _ in range(h)]
        print(count_island(w, h, board))


if __name__ == "__main__":
    main()
