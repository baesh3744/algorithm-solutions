import sys
from collections import deque


MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline


def get_stop_cidx(from_left: bool, ridx: int) -> int:
    cidxes = [cidx for cidx, elem in enumerate(cave[ridx]) if elem == "x"]
    if not cidxes:
        return -1
    return cidxes[0] if from_left else cidxes[-1]


def get_minerals() -> set[tuple[int, int]]:
    minerals: set[tuple[int, int]] = set()
    for ridx, row in enumerate(cave):
        for cidx, elem in enumerate(row):
            if elem == "x":
                minerals.add((ridx, cidx))
    return minerals


def is_range(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < r and 0 <= cidx < c


def get_not_floating(cidx: int) -> set[tuple[int, int]]:
    not_floating: set[tuple[int, int]] = set()
    que: deque[tuple[int, int]] = deque()

    not_floating.add((bottom, cidx))
    que.append((bottom, cidx))

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in MOVES:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx
            next_point: tuple[int, int] = (next_ridx, next_cidx)

            if (
                is_range(*next_point)
                and cave[next_ridx][next_cidx] == "x"
                and next_point not in not_floating
            ):
                not_floating.add(next_point)
                que.append(next_point)

    return not_floating


def get_floating(minerals: set[tuple[int, int]]) -> set[tuple[int, int]]:
    for cidx, elem in enumerate(cave[bottom]):
        if elem == "x" and (bottom, cidx) in minerals:
            minerals.difference_update(get_not_floating(cidx))
    return minerals


def get_falling_dist(floating: set[tuple[int, int]]) -> int:
    falling_dist: int = sys.maxsize
    for ridx, cidx in floating:
        dist: int = 1
        while ridx + dist + 1 < r and cave[ridx + dist + 1][cidx] == ".":
            dist += 1
        falling_dist = min(falling_dist, dist)
    return falling_dist


def fall(floating: set[tuple[int, int]]) -> None:
    for ridx, cidx in floating:
        cave[ridx][cidx] = "."

    dist = get_falling_dist(floating)
    for ridx, cidx in floating:
        cave[ridx + dist][cidx] = "x"


def throw(from_left: bool, ridx: int) -> None:
    cidx = get_stop_cidx(from_left, ridx)
    if cidx == -1:
        return

    cave[ridx][cidx] = "."

    minerals = get_minerals()
    floating = get_floating(minerals)
    if floating:
        fall(floating)


if __name__ == "__main__":
    r, c = map(int, input().split())
    cave = [list(input().strip()) for _ in range(r)]
    n = int(input())
    heights = list(map(int, input().split()))

    bottom: int = r - 1
    for idx, height in enumerate(heights):
        throw(idx & 1 == 0, r - height)

    for row in cave:
        print("".join(row))
