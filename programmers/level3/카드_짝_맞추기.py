import sys
from collections import defaultdict, deque
from itertools import permutations
from typing import DefaultDict, List, Set, Tuple


Point = Tuple[int, int]

SIZE: int = 4
MOVE_LIST: List[Point] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

card_info: DefaultDict[int, List[Point]] = defaultdict(list)


def find_card(board: List[List[int]]) -> None:
    global card_info
    card_info = defaultdict(list)
    for ridx, row in enumerate(board):
        for cidx, elmt in enumerate(row):
            if elmt != 0:
                card_info[elmt].append((ridx, cidx))


def is_range(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < SIZE and 0 <= cidx < SIZE


def ctrl_move(
    board: List[List[int]],
    start: Point,
    move_ridx: int,
    move_cidx: int,
    card_list: Tuple[int, ...],
) -> Point:
    next_ridx, next_cidx = start
    for _ in range(SIZE):
        next_ridx += move_ridx
        next_cidx += move_cidx
        if not is_range(next_ridx, next_cidx):
            break
        if board[next_ridx][next_cidx] in card_list:
            return next_ridx, next_cidx
    return next_ridx - move_ridx, next_cidx - move_cidx


def count(
    board: List[List[int]], start: Point, end: Point, card_list: Tuple[int, ...]
) -> int:
    start_ridx, start_cidx = start
    end_ridx, end_cidx = end

    que: deque[Tuple[int, int, int]] = deque()
    visited: List[List[bool]] = [[False for _ in range(4)] for _ in range(4)]

    que.append((start_ridx, start_cidx, 0))
    visited[start_ridx][start_cidx] = True

    while que:
        cur_ridx, cur_cidx, cur_cnt = que.popleft()

        next_set: Set[Tuple[int, int, int]] = set()
        for move_ridx, move_cidx in MOVE_LIST:
            next_cnt: int = cur_cnt + 1
            next_ridx, next_cidx = cur_ridx + move_ridx, cur_cidx + move_cidx
            if is_range(next_ridx, next_cidx):
                next_set.add((next_ridx, next_cidx, next_cnt))

            next_ridx, next_cidx = ctrl_move(
                board, (cur_ridx, cur_cidx), move_ridx, move_cidx, card_list
            )
            next_set.add((next_ridx, next_cidx, next_cnt))

        for ridx, cidx, cnt in next_set:
            if not visited[ridx][cidx]:
                if ridx == end_ridx and cidx == end_cidx:
                    return cnt
                que.append((ridx, cidx, cnt))
                visited[ridx][cidx] = True
    return 0


def solution(board: List[List[int]], r: int, c: int):
    find_card(board)
    answer: int = sys.maxsize
    for pmt in permutations(card_info.keys()):
        values: List[Tuple[int, Point]] = [(0, (r, c))]
        for index, card in enumerate(pmt):
            _pmt = pmt[index:]
            card1, card2 = card_info[card]
            values = [
                (
                    cnt
                    + count(board, start, card1, _pmt)
                    + count(board, card1, card2, _pmt),
                    card2,
                )
                for cnt, start in values
            ] + [
                (
                    cnt
                    + count(board, start, card2, _pmt)
                    + count(board, card2, card1, _pmt),
                    card1,
                )
                for cnt, start in values
            ]
        answer = min(answer, min(values)[0])
    return answer + 2 * len(card_info)


# 14
print(solution([[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]], 1, 0))
# 16
print(solution([[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]], 0, 1))
