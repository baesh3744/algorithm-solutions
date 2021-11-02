import sys


MOVE_LIST = [(-1, 0), (0, 1), (1, 0), (0, -1)]
START = (0, 0)

TPoint = tuple[int, int]

input = sys.stdin.readline


def count_turnedon(switches: list[list[set[TPoint]]]) -> int:
    que: set[TPoint] = set([START])
    can_go: set[TPoint] = set()
    candidates: set[TPoint] = set()
    turned_on: set[TPoint] = set([START])

    while que:
        ridx, cidx = que.pop()

        can_go.update(switches[ridx][cidx] - turned_on)
        turned_on.update(switches[ridx][cidx])
        candidates.update(
            (ridx + move_ridx, cidx + move_cidx) for move_ridx, move_cidx in MOVE_LIST
        )

        common: set[TPoint] = can_go & candidates
        que.update(common)
        can_go.difference_update(common)
        candidates.difference_update(common)

    return len(turned_on)


def main() -> None:
    n, m = map(int, input().split())

    switches: list[list[set[TPoint]]] = [[set() for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, a, b = map(lambda x: int(x) - 1, input().split())
        switches[x][y].add((a, b))

    print(count_turnedon(switches))


if __name__ == "__main__":
    main()
