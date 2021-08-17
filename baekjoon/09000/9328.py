from collections import deque


Board = list[list[str]]
Point = tuple[int, int]

TARGET: int = 36
MOVE_LIST: list[Point] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def initialize_key_list(key: str) -> None:
    global key_list
    key_list = [False for _ in range(26)]
    if key != "0":
        for alpha in key:
            key_list[ord(alpha) - 97] = True


def find_start() -> list[Point]:
    start_set: set[Point] = set()

    for cidx in range(w):
        for ridx in [0, h - 1]:
            if board[ridx][cidx] != "*":
                start_set.add((ridx, cidx))

    for ridx in range(h):
        for cidx in [0, w - 1]:
            if board[ridx][cidx] != "*":
                start_set.add((ridx, cidx))

    return list(start_set)


def find_key(start: Point, visited: list[list[bool]]) -> tuple[bool, list[list[bool]]]:
    global cnt
    que: deque[Point] = deque()

    block_ord: int = ord(board[start[0]][start[1]])
    if not (65 <= block_ord <= 90) or key_list[block_ord - 65]:
        if block_ord == TARGET:
            cnt += 1
        que.append(start)
        board[start[0]][start[1]] = "."
        visited[start[0]][start[1]] = True

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in MOVE_LIST:
            next_ridx, next_cidx = cur_ridx + move_ridx, cur_cidx + move_cidx

            if (
                not (0 <= next_ridx < h and 0 <= next_cidx < w)
                or board[next_ridx][next_cidx] == "*"
                or visited[next_ridx][next_cidx]
            ):
                continue

            block: str = board[next_ridx][next_cidx]
            block_ord: int = ord(block)

            if 97 <= block_ord <= 122 and not key_list[block_ord - 97]:
                key_list[block_ord - 97] = True
                return True, visited
            if 65 <= block_ord <= 90 and not key_list[block_ord - 65]:
                continue

            if block_ord == TARGET:
                cnt += 1
            que.append((next_ridx, next_cidx))
            board[next_ridx][next_cidx] = "."
            visited[next_ridx][next_cidx] = True

    return False, visited


def count_document(key: str) -> None:
    initialize_key_list(key)
    start_list = find_start()

    has_changed: bool = True
    visited: list[list[bool]] = [[False for _ in range(w)] for _ in range(h)]
    while has_changed:
        has_changed = False
        for start in start_list:
            is_found, visited = find_key(start, visited)
            if is_found:
                visited = [[False for _ in range(w)] for _ in range(h)]
                has_changed = True


def main() -> None:
    global h, w, board, cnt
    t = int(input())
    for _ in range(t):
        h, w = map(int, input().split())
        board = [list(input().strip()) for _ in range(h)]
        key = input().strip()

        cnt = 0
        count_document(key)
        print(cnt)


if __name__ == "__main__":
    main()
