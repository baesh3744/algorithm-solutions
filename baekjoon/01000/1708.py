import sys

Point = tuple[int, int]

input = sys.stdin.readline


def ccw(a: Point, b: Point, c: Point) -> int:
    op: int = a[0] * b[1] + b[0] * c[1] + c[0] * a[1]
    op -= a[1] * b[0] + b[1] * c[0] + c[1] * a[0]
    return op


def monotone_chain(dot_list: list[Point]) -> int:
    upper: list[Point] = []
    lower: list[Point] = []

    dot_list.sort()
    for dot in dot_list:
        while len(upper) > 1 and ccw(upper[-2], upper[-1], dot) <= 0:
            upper.pop()
        while len(lower) > 1 and ccw(lower[-2], lower[-1], dot) >= 0:
            lower.pop()
        upper.append(dot)
        lower.append(dot)
    return len(upper) + len(lower) - 2


def main() -> None:
    n = int(input())
    dot_list = [Point(map(int, input().split())) for _ in range(n)]

    print(monotone_chain(dot_list))


if __name__ == "__main__":
    main()
