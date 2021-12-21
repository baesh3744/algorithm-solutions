import sys
from collections import deque


MAX = sys.maxsize
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline


def isrange(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < n and 0 <= cidx < n


def iscrossed(ridx: int, cidx: int) -> bool:
    cnt_adj: int = 0
    for move_ridx, move_cidx in MOVES:
        next_ridx: int = ridx + move_ridx
        next_cidx: int = cidx + move_cidx
        if isrange(next_ridx, next_cidx) and board[next_ridx][next_cidx] == 0:
            cnt_adj += 1
    return cnt_adj >= 2


def get_time_can_cross(time: int, cycle: int) -> int:
    if time % cycle == 0:
        return time
    return time + cycle - (time % cycle)


def bfs() -> int:
    # 시간, ridx, cidx, 다리를 놓을 수 있는가 (1 - yes, 0 - no)
    que: deque[tuple[int, int, int, int]] = deque()
    visited: list[list[list[int]]] = [
        [[MAX for _ in range(2)] for _ in range(n)] for _ in range(n)
    ]

    que.append((0, 0, 0, 1))
    visited[0][0][1] = 0

    while que:
        time, ridx, cidx, can_build = que.popleft()
        if time > visited[ridx][cidx][can_build]:
            continue

        for move_ridx, move_cidx in MOVES:
            next_ridx: int = ridx + move_ridx
            next_cidx: int = cidx + move_cidx

            if not isrange(next_ridx, next_cidx):
                continue

            if board[ridx][cidx] != 1 and board[next_ridx][next_cidx] != 1:
                continue

            if board[next_ridx][next_cidx] == 0 and (
                can_build == 0 or iscrossed(next_ridx, next_cidx)
            ):
                continue

            next_time: int = time + 1
            next_can_build: int = can_build

            if board[next_ridx][next_cidx] == 0:
                next_time = get_time_can_cross(next_time, m)
                next_can_build = 0
            elif board[next_ridx][next_cidx] >= 2:
                next_time = get_time_can_cross(next_time, board[next_ridx][next_cidx])

            if next_time <= visited[next_ridx][next_cidx][next_can_build]:
                que.append((next_time, next_ridx, next_cidx, next_can_build))
                visited[next_ridx][next_cidx][next_can_build] = next_time

    return min(visited[n - 1][n - 1])


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(bfs())
