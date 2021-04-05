from typing import List
from collections import deque


MOVES: List[List[int]] = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def is_range(N: int, M: int, row: int, col: int) -> bool:
    return 0 <= row < N and 0 <= col < M


def solve(N: int, M: int, K: int) -> int:
    que: 'deque[List[int]]' = deque()

    que.append([0, 0, 0])
    visited[0][0] = [1 for _ in range(K + 1)]

    while que:
        row, col, k = que.popleft()
        count: int = visited[row][col][k] + 1

        if row == N-1 and col == M-1:
            return count - 1

        for move_row, move_col in MOVES:
            next_row: int = row + move_row
            next_col: int = col + move_col

            if not is_range(N, M, next_row, next_col) or visited[next_row][next_col][k]:
                continue

            if board[next_row][next_col] == 0:
                que.append([next_row, next_col, k])
                visited[next_row][next_col][k] = count
            elif k < K:
                que.append([next_row, next_col, k + 1])
                visited[next_row][next_col][k + 1] = count

    return -1


def main() -> None:
    global board, visited
    N, M, K = map(int, input().split())
    board = [[int(ch) for ch in input()] for _ in range(N)]
    visited = [[[0 for _ in range(K + 1)]
                for _ in range(M)] for _ in range(N)]

    print(solve(N, M, K))


if __name__ == "__main__":
    main()
