import sys
from itertools import combinations


input = sys.stdin.readline


def make_snowman_heights(diameters: list[int]) -> list[tuple[int, list[int]]]:
    return sorted(
        (diameters[first] + diameters[second], [first, second])
        for first, second in combinations(range(len(diameters)), 2)
    )


def get_min_diff(heights: list[tuple[int, list[int]]]) -> int:
    min_diff: int = sys.maxsize
    for first, second in zip(heights[:-1], heights[1:]):
        fheight, fdiameters = first
        sheight, sdiameters = second
        diff: int = sheight - fheight
        if diff < min_diff and set(fdiameters).isdisjoint(set(sdiameters)):
            min_diff = diff
    return min_diff


def main() -> None:
    _ = int(input())
    diameters = list(map(int, input().split()))

    heights = make_snowman_heights(diameters)
    print(get_min_diff(heights))


if __name__ == "__main__":
    main()
