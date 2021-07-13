from collections import deque


TBoard = list[deque[int]]
TPoint = tuple[int, int]


def rotate_board(n: int,
                 circle_board: TBoard,
                 x: int, d: int, k: int) -> TBoard:
    dir: int = 1 if d == 0 else -1
    for bnum in range(x, n + 1, x):
        circle_board[bnum - 1].rotate(dir * k)
    return circle_board


def remove_adjacent(n: int,
                    m: int,
                    circle_board: TBoard) -> tuple[TBoard, bool]:
    moves: list[TPoint] = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    is_removed: bool = False
    visited: list[list[bool]] = [[False for _ in range(m)] for _ in range(n)]

    for bidx, board in enumerate(circle_board):
        for vidx, value in enumerate(board):
            needs_removal: bool = False
            que: deque[TPoint] = deque()

            if value != 10000:
                que.append((bidx, vidx))
                visited[bidx][vidx] = True

            while que:
                cur_bidx, cur_vidx = que.popleft()

                for move_bidx, move_vidx in moves:
                    next_bidx: int = cur_bidx + move_bidx
                    next_vidx: int = cur_vidx + move_vidx

                    if next_vidx == -1:
                        next_vidx = m - 1
                    elif next_vidx == m:
                        next_vidx = 0

                    if 0 <= next_bidx < n and \
                            0 <= next_vidx < m and \
                            not visited[next_bidx][next_vidx] and \
                            circle_board[next_bidx][next_vidx] == value:
                        que.append((next_bidx, next_vidx))
                        visited[next_bidx][next_vidx] = True
                        circle_board[next_bidx][next_vidx] = 10000
                        needs_removal = True

            if needs_removal:
                is_removed = True
                circle_board[bidx][vidx] = 10000

    return circle_board, is_removed


def sum_and_count(circle_board: TBoard) -> tuple[int, int]:
    sum_value, cnt_value = 0, 0
    for board in circle_board:
        for value in board:
            if value != 10000:
                cnt_value += 1
                sum_value += value
    return sum_value, cnt_value


def modify_by_avg(circle_board: TBoard) -> TBoard:
    sum_value, cnt_value = sum_and_count(circle_board)
    if cnt_value != 0:
        avg_value: float = sum_value / cnt_value
        for bidx, board in enumerate(circle_board):
            for vidx, value in enumerate(board):
                if value == 10000:
                    continue
                elif float(value) > avg_value:
                    circle_board[bidx][vidx] -= 1
                elif float(value) < avg_value:
                    circle_board[bidx][vidx] += 1
    return circle_board


def main() -> None:
    n, m, t = map(int, input().split())
    circle_board = [deque(map(int, input().split())) for _ in range(n)]

    for _ in range(t):
        x, d, k = map(int, input().split())
        circle_board = rotate_board(n, circle_board, x, d, k)
        circle_board, is_removed = remove_adjacent(n, m, circle_board)
        if not is_removed:
            circle_board = modify_by_avg(circle_board)

    sum_value, _ = sum_and_count(circle_board)
    print(sum_value)


if __name__ == "__main__":
    main()
