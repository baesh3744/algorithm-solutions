import sys
from copy import deepcopy
from itertools import combinations


MAX = sys.maxsize

Point = tuple[int, int]

input = sys.stdin.readline


def get_enemy_set() -> set[Point]:
    enemy_set: set[Point] = set()
    for ridx, row in enumerate(board):
        for cidx, elem in enumerate(row):
            if elem == 1:
                enemy_set.add((ridx, cidx))
    return enemy_set


def get_target(enemy_set: set[Point], archer: int) -> Point:
    target: tuple[int, int] = tuple()
    target_distance: int = MAX

    for ridx, cidx in enemy_set:
        distance: int = (archer_ridx - ridx) + abs(archer - cidx)
        if distance <= d and (
            distance < target_distance
            or (target_distance == distance and cidx < target[1])
        ):
            target_distance = distance
            target = (ridx, cidx)

    return target


def move(enemy_set: set[Point]) -> set[Point]:
    return set((ridx + 1, cidx) for ridx, cidx in enemy_set if ridx < n - 1)


def play(enemy_set: set[Point], archer_list: tuple[int, int, int]) -> int:
    removed: int = 0

    while enemy_set:
        target_set: set[Point] = set()
        for archer in archer_list:
            target = get_target(enemy_set, archer)
            if target:
                target_set.add(target)

        removed += len(target_set)
        enemy_set.difference_update(target_set)

        enemy_set = move(enemy_set)

    return removed


def solve(enemy_set: set[Point]) -> int:
    max_removed: int = 0
    for archer_list in combinations(range(m), 3):
        removed = play(deepcopy(enemy_set), archer_list)
        max_removed = max(max_removed, removed)
    return max_removed


if __name__ == "__main__":
    n, m, d = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    archer_ridx: int = n
    enemy_set = get_enemy_set()
    print(solve(enemy_set))
