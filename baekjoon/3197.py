import sys
from collections import deque
from typing import List, Deque, Tuple


MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

Point = Tuple[int, int]

input = sys.stdin.readline


def init() -> Tuple[Point, Deque[Point]]:
    start: Point = tuple()
    waters: Deque[Point] = deque()

    for ridx, row in enumerate(board):
        for cidx, elem in enumerate(row):
            if elem == "L":
                start = (ridx, cidx)
            if elem != "X":
                waters.append((ridx, cidx))

    return start, waters


def isrange(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < r and 0 <= cidx < c


def get_adjs(ridx: int, cidx: int) -> List[Point]:
    return [
        (ridx + mridx, cidx + mcidx)
        for mridx, mcidx in MOVES
        if isrange(ridx + mridx, cidx + mcidx)
    ]


def bfs(que: Deque[Point]) -> Tuple[bool, Deque[Point]]:
    next_que: Deque[Point] = deque()

    while que:
        ridx, cidx = que.popleft()

        for adj_ridx, adj_cidx in get_adjs(ridx, cidx):
            if visited[adj_ridx][adj_cidx]:
                continue

            visited[adj_ridx][adj_cidx] = True
            if board[adj_ridx][adj_cidx] == "L":
                return True, que
            elif board[adj_ridx][adj_cidx] == "X":
                next_que.append((adj_ridx, adj_cidx))
            else:
                que.append((adj_ridx, adj_cidx))

    return False, next_que


def melt(waters: Deque[Point]) -> Deque[Point]:
    next_waters: Deque[Point] = deque()

    while waters:
        ridx, cidx = waters.pop()

        for adj_ridx, adj_cidx in get_adjs(ridx, cidx):
            if board[adj_ridx][adj_cidx] == "X":
                board[adj_ridx][adj_cidx] = "."
                next_waters.append((adj_ridx, adj_cidx))

    return next_waters


def solve() -> int:
    day: int = 0

    start, waters = init()
    que: Deque[Point] = deque([start])

    sridx, scidx = start
    board[sridx][scidx] = "."
    visited[sridx][scidx] = True

    while True:
        ismet, que = bfs(que)
        if ismet:
            break
        waters = melt(waters)
        day += 1

    return day


if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]

    visited = [[False for _ in range(c)] for _ in range(r)]
    print(solve())
