import sys


MAX = sys.maxsize
MOVE_LIST = [(0, 1), (-1, 0), (0, -1), (1, 0)]

Point = tuple[int, int]

input = sys.stdin.readline


def ccw(a: Point, b: Point, c: Point) -> int:
    op: int = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    op -= a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return op


def is_intersect(a: Point, b: Point, c: Point, d: Point) -> tuple[bool, bool]:
    ab = ccw(a, b, c) * ccw(a, b, d)
    cd = ccw(c, d, a) * ccw(c, d, b)
    if ab == 0 and cd == 0:
        if a > b:
            a, b = b, a
        if c > d:
            c, d = d, c
        return c <= b and a <= d, True
    return ab <= 0 and cd <= 0, False


def calc_time_to_meet(is_parallel: bool, xy: int, a: Point, c: Point, d: Point) -> int:
    time: int = abs(c[xy] - a[xy])
    if is_parallel:
        time = min(time, abs(d[xy] - a[xy]))
    return time


def calc_out_time(l: int, x: int, y: int) -> int:
    return max(0 - x, 0 - y, x - 2 * l, y - 2 * l)


def calc_time_to_die(
    l: int, turning_points: list[Point], move_inputs: list[tuple[int, str]]
) -> int:
    time: int = 0

    for idx, point in enumerate(turning_points[1:], 1):
        is_dead: bool = False
        move_time: int = move_inputs[idx - 1][0]

        if (out_time := calc_out_time(l, *point)) > 0:
            is_dead = True
            move_time -= out_time - 1

        if idx >= 3:
            prev = turning_points[idx - 1]
            for sidx, end in enumerate(turning_points[1 : idx - 1]):
                start = turning_points[sidx]
                is_intersected, is_parallel = is_intersect(prev, point, start, end)
                if is_intersected:
                    is_dead = True
                    move_time = min(
                        move_time,
                        calc_time_to_meet(is_parallel, idx & 1, prev, start, end),
                    )

        time += move_time
        if is_dead:
            break

    return time


def list_turning_points(
    l: int, n: int, move_inputs: list[tuple[int, str]]
) -> list[Point]:
    head: int = 0
    turning_points: list[Point] = [(l, l) for _ in range(n + 2)]
    for idx, (t, dir) in enumerate(move_inputs, 1):
        last_y, last_x = turning_points[idx - 1]
        move_y, move_x = MOVE_LIST[head]
        turning_points[idx] = (last_y + move_y * t, last_x + move_x * t)
        head = (head + (1 if dir == "L" else -1) + 4) % 4
    return turning_points


def main() -> None:
    l = int(input())
    n = int(input())

    move_inputs: list[tuple[int, str]] = [tuple() for _ in range(n + 1)]
    for idx in range(n):
        t, dir = input().split()
        move_inputs[idx] = (int(t), dir)
    move_inputs[n] = (3 * l, "L")

    turning_points = list_turning_points(l, n, move_inputs)
    time = calc_time_to_die(l, turning_points, move_inputs)
    print(time)


if __name__ == "__main__":
    main()
