import copy
from collections import deque


def get_turning_gears(gears: list[deque[int]], num: int) -> list[int]:
    turning_gears: list[int] = []

    left_idx: int = num - 1
    while 0 <= left_idx and (gears[left_idx][2] != gears[left_idx + 1][-2]):
        turning_gears.append(left_idx)
        left_idx -= 1

    right_idx: int = num + 1
    while right_idx < 4 and (gears[right_idx - 1][2] != gears[right_idx][-2]):
        turning_gears.append(right_idx)
        right_idx += 1

    return turning_gears


def turn_gears(gears: list[deque[int]], num: int, dir: int) -> list[deque[int]]:
    turning_gears: list[int] = get_turning_gears(gears, num)

    gears[num].rotate(dir)
    for gear_idx in turning_gears:
        cur_dir: int = dir if abs(gear_idx - num) % 2 == 0 else -1 * dir
        gears[gear_idx].rotate(cur_dir)

    return gears


def get_final_gears(gears: list[deque[int]], turns: list[tuple[int, int]]) -> list[deque[int]]:
    final_gears: list[deque[int]] = copy.deepcopy(gears)

    for num, dir in turns:
        final_gears = turn_gears(final_gears, num - 1, dir)

    return final_gears


def main() -> None:
    gears: list[deque[int]] = []
    for _ in range(4):
        gear = deque(map(int, input()))
        gears.append(gear)
    k = int(input())
    turns: list[tuple[int, int]] = []
    for _ in range(k):
        num, dir = map(int, input().split())
        turns.append((num, dir))

    final_gears = get_final_gears(gears, turns)

    score: int = 0
    for idx in range(4):
        if final_gears[idx][0] == 1:
            score += 2 ** idx
    print(score)


if __name__ == "__main__":
    main()
