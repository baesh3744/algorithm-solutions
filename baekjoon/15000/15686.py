import sys
from itertools import combinations
from typing import Final


Point = tuple[int, int]
INF: Final[int] = sys.maxsize


def get_non_empty(n: int, board: list[list[int]]) -> tuple[list[Point], list[Point]]:
    houses: list[Point] = []
    chickens: list[Point] = []

    for ridx in range(n):
        for cidx in range(n):
            if board[ridx][cidx] == 1:
                houses.append((ridx, cidx))
            elif board[ridx][cidx] == 2:
                chickens.append((ridx, cidx))

    return houses, chickens


def calc_min_city_cdistance(m: int, houses: list[Point], chickens: list[Point]) -> int:
    city_cdistance: int = INF

    for survived in combinations(chickens, m):
        cdistance: int = 0

        for house in houses:
            cdistance += min([abs(house[0] - sur[0]) + abs(house[1] - sur[1])
                              for sur in survived])
            if city_cdistance <= cdistance:
                break

        city_cdistance = min(city_cdistance, cdistance)

    return city_cdistance


def main() -> None:
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    houses, chickens = get_non_empty(n, board)
    print(calc_min_city_cdistance(m, houses, chickens))


if __name__ == "__main__":
    main()
