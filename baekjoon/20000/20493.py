import sys


# 0: 우, 1: 하, 2: 좌, 3: 상
NEXT_DIR: dict[str, list[int]] = {"right": [1, 2, 3, 0], "left": [3, 0, 1, 2]}
MOVE_LIST: list[tuple[int, int]] = [(1, 0), (0, -1), (-1, 0), (0, 1)]

input = sys.stdin.readline


def get_next_location(x: int, y: int, dir: int, dist: int) -> tuple[int, int]:
    move_x, move_y = MOVE_LIST[dir]
    return x + dist * move_x, y + dist * move_y


def main() -> None:
    n, t = map(int, input().split())

    x, y, dir, prev_time = 0, 0, 0, 0
    for _ in range(n):
        ti, si = input().split()
        x, y = get_next_location(x, y, dir, int(ti) - prev_time)
        dir = NEXT_DIR[si][dir]
        prev_time = int(ti)
    x, y = get_next_location(x, y, dir, t - prev_time)
    print(x, y)


if __name__ == "__main__":
    main()
