import copy
import sys
from typing import List, Tuple


Room = List[List[int]]


def find_air_cleaner(r: int, room: Room) -> int:
    ridx: int = 0
    while ridx < r - 1 and room[ridx][0] != -1:
        ridx += 1
    return ridx


def is_range(r: int, c: int, ridx: int, cidx: int) -> bool:
    return 0 <= ridx < r and 0 <= cidx < c


def spread_dust(r: int, c: int, room: Room) -> Room:
    moves: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    new_room: Room = copy.deepcopy(room)

    for ridx in range(r):
        for cidx in range(c):
            if room[ridx][cidx] > 0:
                next_dust: int = room[ridx][cidx] // 5

                for move_ridx, move_cidx in moves:
                    next_ridx: int = ridx + move_ridx
                    next_cidx: int = cidx + move_cidx
                    if (is_range(r, c, next_ridx, next_cidx) and
                            room[next_ridx][next_cidx] != -1):
                        new_room[ridx][cidx] -= next_dust
                        new_room[next_ridx][next_cidx] += next_dust

    return new_room


def clean_air_upper(c: int, air_cleaner: int, room: Room) -> Room:
    for ridx in range(air_cleaner - 1, 0, -1):
        room[ridx][0] = room[ridx - 1][0]

    for cidx in range(c - 1):
        room[0][cidx] = room[0][cidx + 1]

    for ridx in range(air_cleaner):
        room[ridx][c - 1] = room[ridx + 1][c - 1]

    for cidx in range(c - 1, 1, -1):
        room[air_cleaner][cidx] = room[air_cleaner][cidx - 1]
    room[air_cleaner][1] = 0

    return room


def clean_air_lower(r: int, c: int, air_cleaner: int, room: Room) -> Room:
    for ridx in range(air_cleaner + 1, r - 1):
        room[ridx][0] = room[ridx + 1][0]

    for cidx in range(c - 1):
        room[r - 1][cidx] = room[r - 1][cidx + 1]

    for ridx in range(r - 1, air_cleaner, -1):
        room[ridx][c - 1] = room[ridx - 1][c - 1]

    for cidx in range(c - 1, 1, -1):
        room[air_cleaner][cidx] = room[air_cleaner][cidx - 1]
    room[air_cleaner][1] = 0

    return room


def do(r: int, c: int, t: int, air_cleaner: int, room: Room) -> Room:
    if t == 0:
        return room

    room = spread_dust(r, c, room)
    room = clean_air_upper(c, air_cleaner, room)
    room = clean_air_lower(r, c, air_cleaner + 1, room)

    return do(r, c, t - 1, air_cleaner, room)


def sum_room(room: Room) -> int:
    return sum([sum(row) for row in room])


def main() -> None:
    r, c, t = map(int, input().split())
    room = [list(map(int, input().split())) for _ in range(r)]

    air_cleaner = find_air_cleaner(r, room)
    room = do(r, c, t, air_cleaner, room)
    print(sum_room(room) + 2)


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
