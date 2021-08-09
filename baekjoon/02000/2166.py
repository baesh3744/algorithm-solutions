import sys


input = sys.stdin.readline


def main() -> None:
    n = int(input())
    coords = [tuple(map(int, input().split())) for _ in range(n)]

    coords.append(coords[0])
    area: int = 0
    for index, (x, y) in enumerate(coords[:-1]):
        area += (x + coords[index + 1][0]) * (y - coords[index + 1][1])
    print("%.1f" % abs(area / 2))


if __name__ == "__main__":
    main()
