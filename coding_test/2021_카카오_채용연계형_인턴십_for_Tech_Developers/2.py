from collections import deque
from typing import List, Tuple


def is_range(ridx: int, cidx: int) -> bool:
    return (0 <= ridx < 5 and 0 <= cidx < 5)


def has_distance(board: List[List[str]], ridx: int, cidx: int) -> bool:
    moves: List[Tuple[int, int]] = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    visited: List[List[bool]] = [[False for _ in range(5)] for _ in range(5)]
    que: deque[Tuple[int, int, int]] = deque()

    que.append((2, ridx, cidx))
    visited[ridx][cidx] = True
    while que:
        cur_dist, cur_ridx, cur_cidx = que.popleft()

        for move_row, move_col in moves:
            next_ridx: int = cur_ridx + move_row
            next_cidx: int = cur_cidx + move_col

            if is_range(next_ridx, next_cidx) and not visited[next_ridx][next_cidx]:
                if board[next_ridx][next_cidx] == 'P':
                    return False

                if board[next_ridx][next_cidx] == 'O' and cur_dist == 2:
                    que.append((cur_dist - 1, next_ridx, next_cidx))
                    visited[next_ridx][next_cidx] = True
    return True


def check_place(place: List[str]) -> int:
    board: List[List[str]] = [[ch for ch in row] for row in place]

    for ridx in range(5):
        for cidx in range(5):
            if board[ridx][cidx] == 'P' and not has_distance(board, ridx, cidx):
                return 0
    return 1


def solution(places: List[List[str]]):
    answer: List[int] = []

    for place in places:
        answer.append(check_place(place))

    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"],
                ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"],
                ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"],
                ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"],
                ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))
