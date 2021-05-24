import math
from typing import List


def initialize_has_hlines(n: int, h: int, hlines: List[List[int]]) -> List[List[bool]]:
    has_hlines: List[List[bool]] = [
        [False for _ in range(n + 2)] for _ in range(h + 1)]
    for location, ladder in hlines:
        has_hlines[location][ladder] = True
    return has_hlines


def do_ghost_leg(ladder: int, h: int, has_hlines: List[List[bool]]) -> int:
    for location in range(h + 1):
        if has_hlines[location][ladder - 1]:
            ladder -= 1
        elif has_hlines[location][ladder]:
            ladder += 1
    return ladder


def needs_hline(n: int, h: int, has_hlines: List[List[bool]]) -> bool:
    for ladder in range(1, n + 1):
        if ladder != do_ghost_leg(ladder, h, has_hlines):
            return True
    return False


def can_manipulate(n: int, h: int, last_added_idx: int, cnt_added: int, has_hlines: List[List[bool]]) -> bool:
    needs = needs_hline(n, h, has_hlines)
    if not needs:
        return True
    if needs and cnt_added == 0:
        return False

    for idx in range(last_added_idx + 1, n * h + 1):
        location: int = math.ceil(idx / n)
        ladder: int = idx - n * (location - 1)

        if (has_hlines[location][ladder] or
                has_hlines[location][ladder - 1] or
                has_hlines[location][ladder + 1]):
            continue

        has_hlines[location][ladder] = True
        if can_manipulate(n, h, idx, cnt_added - 1, has_hlines):
            return True
        has_hlines[location][ladder] = False

    return False


def main() -> None:
    n, m, h = map(int, input().split())
    hlines = [list(map(int, input().split())) for _ in range(m)]

    has_hlines = initialize_has_hlines(n, h, hlines)
    answer: int = -1
    for cnt_added in range(4):
        if can_manipulate(n, h, 0, cnt_added, has_hlines):
            answer = cnt_added
            break
    print(answer)


if __name__ == "__main__":
    main()
