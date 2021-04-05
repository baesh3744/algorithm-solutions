from typing import Deque, List, Tuple
from collections import deque


def is_range(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < m and 0 <= cidx < n


def get_area(ridx: int, cidx: int, rnum: int) -> int:
    moves: List[Tuple[int, int, int]] = [
        (0, -1, 1), (-1, 0, 2), (0, 1, 4), (1, 0, 8)]
    que: Deque[Tuple[int, int]] = deque()
    area: int = 0

    que.append((ridx, cidx))
    room[ridx][cidx] = rnum
    while que:
        cur_ridx, cur_cidx = que.popleft()
        area += 1

        for move_ridx, move_cidx, dir in moves:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if (is_range(next_ridx, next_cidx)
                    and room[next_ridx][next_cidx] == -1
                    and not castle[cur_ridx][cur_cidx] & dir):
                que.append((next_ridx, next_cidx))
                room[next_ridx][next_cidx] = rnum

    return area


def get_areas() -> List[int]:
    areas: List[int] = []

    for ridx in range(m):
        for cidx in range(n):
            if room[ridx][cidx] == -1:
                areas.append(get_area(ridx, cidx, len(areas)))

    return areas


def get_max_2areas(areas: List[int]) -> int:
    max_2areas: int = 0

    for ridx in range(m):
        for cidx in range(n):
            if ridx != m - 1 and room[ridx][cidx] != room[ridx + 1][cidx]:
                area1: int = areas[room[ridx][cidx]]
                area2: int = areas[room[ridx + 1][cidx]]
                max_2areas = max(max_2areas, area1 + area2)

            if cidx != n - 1 and room[ridx][cidx] != room[ridx][cidx + 1]:
                area1: int = areas[room[ridx][cidx]]
                area2: int = areas[room[ridx][cidx + 1]]
                max_2areas = max(max_2areas, area1 + area2)

    return max_2areas


def main() -> None:
    global n, m, castle, room
    n, m = map(int, input().split())
    castle = [list(map(int, input().split())) for _ in range(m)]
    room = [[-1 for _ in range(n)] for _ in range(m)]

    areas: List[int] = get_areas()
    max_2areas: int = get_max_2areas(areas)
    areas.sort(reverse=True)
    print(len(areas))
    print(areas[0])
    print(max_2areas)


if __name__ == "__main__":
    main()
