import sys
from collections import deque
from typing import List, Tuple


Board = List[List[int]]
Point = Tuple[int, int]

MOVES: List[Point] = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def is_range(n: int, ridx: int, cidx: int) -> bool:
    return 0 <= ridx < n and 0 <= cidx < n


def check_union(ridx: int, cidx: int,
                union_idx: int,
                checked: Board,
                populations: Board) -> Tuple[Board, int]:
    que: deque[Point] = deque()

    que.append((ridx, cidx))
    checked[ridx][cidx] = union_idx
    sum_union: int = populations[ridx][cidx]
    cnt_union: int = 1

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in MOVES:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if (is_range(n, next_ridx, next_cidx)
                    and checked[next_ridx][next_cidx] == -1
                    and l <= abs(populations[cur_ridx][cur_cidx] - populations[next_ridx][next_cidx]) <= r):
                que.append((next_ridx, next_cidx))
                checked[next_ridx][next_cidx] = union_idx
                sum_union += populations[next_ridx][next_cidx]
                cnt_union += 1

    return checked, sum_union // cnt_union


def move_populations(union_populations: List[int],
                     checked: Board) -> Board:
    new_populations: Board = [[-1 for _ in range(n)] for _ in range(n)]
    for ridx in range(n):
        for cidx in range(n):
            new_populations[ridx][cidx] = union_populations[checked[ridx][cidx]]
    return new_populations


def count_movement(populations: Board) -> int:
    checked: Board = [[-1 for _ in range(n)] for _ in range(n)]
    union_populations: List[int] = []

    for ridx in range(n):
        for cidx in range(n):
            if checked[ridx][cidx] == -1:
                checked, union_population = check_union(
                    ridx, cidx, len(union_populations), checked, populations)
                union_populations.append(union_population)

    if len(union_populations) == n * n:
        return 0

    new_populations = move_populations(union_populations, checked)
    return 1 + count_movement(new_populations)


def main() -> None:
    global n, l, r
    n, l, r = map(int, input().split())
    populations = [list(map(int, input().split())) for _ in range(n)]

    print(count_movement(populations))


if __name__ == "__main__":
    sys.setrecursionlimit(3000)
    main()
