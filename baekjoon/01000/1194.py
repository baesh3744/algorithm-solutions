from collections import deque


def find_zero(maze: list[list[str]]) -> tuple[int, int]:
    zero_ridx, zero_cidx = -1, -1
    for ridx, row in enumerate(maze):
        for cidx, value in enumerate(row):
            if value == '0':
                zero_ridx, zero_cidx = ridx, cidx
    return zero_ridx, zero_cidx


def count_turn(n: int, m: int, maze: list[list[str]]) -> int:
    moves: list[tuple[int, int]] = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    que: deque[tuple[int, int, int]] = deque()
    visited: list[list[list[int]]] \
        = [[[0 for _ in range(64)] for _ in range(m)] for _ in range(n)]

    zero_ridx, zero_cidx = find_zero(maze)

    que.append((zero_ridx, zero_cidx, 0))
    visited[zero_ridx][zero_cidx][0] = 0

    while que:
        cur_ridx, cur_cidx, cur_status = que.popleft()

        for move_ridx, move_cidx in moves:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if 0 <= next_ridx < n and \
                    0 <= next_cidx < m and \
                    not visited[next_ridx][next_cidx][cur_status] and \
                    maze[next_ridx][next_cidx] != '#':
                value: str = maze[next_ridx][next_cidx]
                next_turn: int = visited[cur_ridx][cur_cidx][cur_status] + 1
                if value == '1':
                    return next_turn
                elif 'a' <= value <= 'f':
                    next_status: int \
                        = cur_status | (1 << ord(value) - ord('a'))
                    que.append((next_ridx, next_cidx, next_status))
                    visited[next_ridx][next_cidx][next_status] = next_turn
                elif 'A' <= value <= 'F' and \
                        not (cur_status & (1 << ord(value) - ord('A'))):
                    continue
                que.append((next_ridx, next_cidx, cur_status))
                visited[next_ridx][next_cidx][cur_status] = next_turn

    return -1


def main() -> None:
    n, m = map(int, input().split())
    maze = [list(input()) for _ in range(n)]

    print(count_turn(n, m, maze))


if __name__ == "__main__":
    main()
