from typing import Final, List, Tuple
from collections import deque


MOVES: Final[List[Tuple[int, int]]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def check_room(ridx: int, cidx: int, rnum: int) -> None:
    area: int = 0
    que: 'deque[Tuple[int, int]]' = deque()

    que.append((ridx, cidx))
    room[ridx][cidx] = rnum
    area += 1
    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in MOVES:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if (0 <= next_ridx < N and 0 <= next_cidx < M
                    and board[next_ridx][next_cidx] == 0
                    and room[next_ridx][next_cidx] == -1):
                que.append((next_ridx, next_cidx))
                room[next_ridx][next_cidx] = rnum
                area += 1

    areas.append(area)


def calc_area() -> Tuple[List[List[int]], List[int]]:
    for ridx in range(N):
        for cidx in range(M):
            if board[ridx][cidx] == 0 and room[ridx][cidx] == -1:
                check_room(ridx, cidx, len(areas))

    return room, areas


def get_area(ridx: int, cidx: int) -> int:
    area: int = 0
    rooms: List[int] = []

    for move_ridx, move_cidx in MOVES:
        next_ridx: int = ridx + move_ridx
        next_cidx: int = cidx + move_cidx

        if (0 <= next_ridx < N and 0 <= next_cidx < M
                and board[next_ridx][next_cidx] == 0):
            rooms.append(room[next_ridx][next_cidx])

    rooms = list(set(rooms))
    for rnum in rooms:
        area += areas[rnum]

    return (area + 1) % 10


def print_ans() -> None:
    for ridx in range(N):
        for cidx in range(M):
            if board[ridx][cidx] == 0:
                print(0, end='')
            else:
                print(get_area(ridx, cidx), end='')
        print()


def main() -> None:
    global N, M, board, room, areas
    N, M = map(int, input().split())
    board = [[int(ch) for ch in input()] for _ in range(N)]
    room = [[-1 for _ in range(M)] for _ in range(N)]
    areas = [0]

    calc_area()
    print_ans()


if __name__ == "__main__":
    main()
