from typing import Final
import sys


MAX: Final[int] = 1000000


def color_house(N: int, color: int, init_color: int) -> int:
    if N == 1:
        return rgb[N][color] if color != init_color else MAX
    if cache[N][color] != -1:
        return cache[N][color]

    ret: int = MAX
    for next_color in range(3):
        if next_color != color:
            ret = min(ret, color_house(
                N - 1, next_color, init_color) + rgb[N][color])
    cache[N][color] = ret
    return ret


def main() -> None:
    global rgb, cache
    N = int(input())
    rgb = [list(map(int, input().split())) for _ in range(N)]

    rgb.insert(0, [0, 0, 0])

    min_cost: int = MAX
    for color in range(3):
        cache = [[-1, -1, -1] for _ in range(N + 1)]
        min_cost = min(min_cost, color_house(N, color, color))
    print(min_cost)


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
