import sys
from collections import deque


MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
Point = tuple[int, int]
input = sys.stdin.readline


def isrange(y: int, x: int) -> bool:
    return 0 <= y < 12 and 0 <= x < 6


def bfs(start_y: int, start_x: int, color: str) -> list[Point]:
    group: list[Point] = []
    que: deque[Point] = deque()

    group.append((start_y, start_x))
    que.append((start_y, start_x))
    visited[start_y][start_x] = True

    while que:
        y, x = que.popleft()

        for move_y, move_x in MOVES:
            adj_y: int = y + move_y
            adj_x: int = x + move_x

            if (
                not isrange(adj_y, adj_x)
                or visited[adj_y][adj_x]
                or board[adj_y][adj_x] != color
            ):
                continue

            group.append((adj_y, adj_x))
            que.append((adj_y, adj_x))
            visited[adj_y][adj_x] = True

    return group


def remove(group: list[Point]) -> None:
    for y, x in group:
        board[y][x] = "."


def fall_puyo(x: int) -> None:
    ptr: int = 11

    for y in range(11, -1, -1):
        if board[y][x] != ".":
            board[ptr][x] = board[y][x]
            ptr -= 1

    for y in range(ptr + 1):
        board[y][x] = "."


def count() -> int:
    global visited
    cnt: int = 0

    while True:
        has_group: bool = False
        visited = [[False for _ in range(6)] for _ in range(12)]

        for y in range(12):
            for x in range(6):
                if board[y][x] == "." or visited[y][x]:
                    continue

                group = bfs(y, x, board[y][x])
                if len(group) >= 4:
                    has_group = True
                    remove(group)

        if not has_group:
            break

        cnt += 1
        for x in range(6):
            fall_puyo(x)

    return cnt


if __name__ == "__main__":
    board = [list(input().strip()) for _ in range(12)]

    visited: list[list[bool]] = []
    print(count())
