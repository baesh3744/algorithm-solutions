import sys
from collections import deque


MOVE_LIST: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline


def move(r: int, c: int, board: list[list[int]]) -> int:
    turn: int = 0
    que: deque[tuple[int, int, int]] = deque()
    visited: list[list[set[int]]] = [[set() for _ in range(c)] for _ in range(r)]

    que.append((0, 0, board[0][0]))
    visited[0][0].add(board[0][0])

    while que:
        turn += 1
        for _ in range(len(que)):
            cur_r, cur_c, cur_status = que.popleft()

            for move_r, move_c in MOVE_LIST:
                next_r, next_c = cur_r + move_r, cur_c + move_c

                if (
                    0 <= next_r < r
                    and 0 <= next_c < c
                    and not cur_status & board[next_r][next_c]
                ):
                    next_status = cur_status | board[next_r][next_c]
                    if next_status not in visited[next_r][next_c]:
                        que.append((next_r, next_c, next_status))
                        visited[next_r][next_c].add(next_status)

    return turn


def main() -> None:
    r, c = map(int, input().split())
    board = [list(map(lambda x: 1 << (ord(x) - 65), input().strip())) for _ in range(r)]

    print(move(r, c, board))


if __name__ == "__main__":
    main()
