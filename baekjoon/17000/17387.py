Point = tuple[int, int]


def ccw(a: Point, b: Point, c: Point) -> int:
    op: int = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    op -= a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return op


def is_intersect(a: Point, b: Point, c: Point, d: Point) -> bool:
    ccw_ab: int = ccw(a, b, c) * ccw(a, b, d)
    ccw_cd: int = ccw(c, d, a) * ccw(c, d, b)
    if ccw_ab == 0 and ccw_cd == 0:
        if a < b:
            a, b = b, a
        if c < d:
            c, d = d, c
        return d <= a and b <= c
    return ccw_ab <= 0 and ccw_cd <= 0


def main() -> None:
    x1, y1, x2, y2 = map(int, input().split())
    x3, y3, x4, y4 = map(int, input().split())

    print(1 if is_intersect((x1, y1), (x2, y2), (x3, y3), (x4, y4)) else 0)


if __name__ == "__main__":
    main()
