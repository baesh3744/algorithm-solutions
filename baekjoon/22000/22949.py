import sys
from collections import deque
from typing import List, Tuple


Board = List[List[str]]
Point = Tuple[int, int]

DIR_SIZE: int = 4
SECTION_SIZE: int = 4
MAX: int = sys.maxsize
NOT_FOUND_START: Point = (-1, -1)
MOVE_LIST: List[Point] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline


def find_start(board: Board) -> Point:
    for ridx, row in enumerate(board):
        for cidx, elmt in enumerate(row):
            if elmt == "S":
                return ridx, cidx
    return NOT_FOUND_START


def is_range(k: int, ridx: int, cidx: int) -> bool:
    return 0 <= ridx < SECTION_SIZE * k and 0 <= cidx < SECTION_SIZE * k


def turn_point_90(ridx: int, cidx: int) -> Point:
    sridx: int = (ridx // SECTION_SIZE) * SECTION_SIZE
    scidx: int = (cidx // SECTION_SIZE) * SECTION_SIZE
    return sridx + (cidx - scidx), scidx + 3 - (ridx - sridx)


def turn_point(ridx: int, cidx: int, cnt: int) -> Point:
    turned_ridx, turned_cidx = ridx, cidx
    for _ in range(cnt):
        turned_ridx, turned_cidx = turn_point_90(turned_ridx, turned_cidx)
    return turned_ridx, turned_cidx


def get_section(k: int, ridx: int, cidx: int) -> int:
    return k * (ridx // SECTION_SIZE) + (cidx // SECTION_SIZE)


def move(k: int, board: Board) -> int:
    start_ridx, start_cidx = find_start(board)
    cache[start_ridx][start_cidx][0] = 0

    que: deque[Tuple[Point, int, int, int]] = deque()

    section = get_section(k, start_ridx, start_cidx)
    que.append(((start_ridx, start_cidx), 0, 0, section))

    while que:
        (cur_ridx, cur_cidx), cur_dir, cur_dist, cur_section = que.popleft()

        next_dir: int = (cur_dir + 1) % DIR_SIZE
        next_dist: int = cur_dist + 1

        if next_dist < cache[cur_ridx][cur_cidx][next_dir]:
            cache[cur_ridx][cur_cidx][next_dir] = next_dist
            que.append(((cur_ridx, cur_cidx), next_dir, next_dist, cur_section))

        turned_ridx, turned_cidx = turn_point(cur_ridx, cur_cidx, cur_dir)
        for move_ridx, move_cidx in MOVE_LIST:
            next_ridx: int = turned_ridx + move_ridx
            next_cidx: int = turned_cidx + move_cidx

            if not is_range(k, next_ridx, next_cidx):
                continue

            next_section = get_section(k, next_ridx, next_cidx)
            if cur_section == next_section:
                next_dir = (cur_dir + 1) % DIR_SIZE
                next_ridx, next_cidx = turn_point(
                    next_ridx, next_cidx, DIR_SIZE - cur_dir
                )
            else:
                next_dir = 1

            if (
                board[next_ridx][next_cidx] != "#"
                and next_dist < cache[next_ridx][next_cidx][next_dir]
            ):
                if board[next_ridx][next_cidx] == "E":
                    return next_dist

                cache[next_ridx][next_cidx][next_dir] = next_dist
                que.append(((next_ridx, next_cidx), next_dir, next_dist, next_section))

    return -1


def main() -> None:
    global cache
    k = int(input())
    board: Board = [list(input().strip()) for _ in range(SECTION_SIZE * k)]
    cache = [
        [[MAX for _ in range(DIR_SIZE)] for _ in range(SECTION_SIZE * k)]
        for _ in range(SECTION_SIZE * k)
    ]
    print(move(k, board))


if __name__ == "__main__":
    main()
