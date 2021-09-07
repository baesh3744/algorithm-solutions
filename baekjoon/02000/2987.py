import sys
from typing import Callable

Point = tuple[int, int]

input = sys.stdin.readline
mi_input: Callable[[], Point] = lambda: Point(map(int, input().split()))


def ccw(a: Point, b: Point, c: Point) -> int:
    op = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    op -= a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return op


def get_inside(a: Point, b: Point, c: Point, point_list: list[Point]) -> list[Point]:
    inside_list: list[Point] = []
    base_ccw = ccw(a, b, c)
    for point in point_list:
        if base_ccw * ccw(a, b, point) >= 0:
            inside_list.append(point)
    return inside_list


def main() -> None:
    a = mi_input()
    b = mi_input()
    c = mi_input()
    n = int(input())
    point_list = [mi_input() for _ in range(n)]

    print("%.1f" % (abs(ccw(a, b, c)) / 2))

    apple_tree = get_inside(a, b, c, point_list)
    apple_tree = get_inside(b, c, a, apple_tree)
    apple_tree = get_inside(c, a, b, apple_tree)
    print(len(apple_tree))


if __name__ == "__main__":
    main()
