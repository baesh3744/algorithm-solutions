import heapq
import sys
from collections import deque


MOVE_LIST = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline

bridge_list: list[list[tuple[int, int]]]


def is_connected(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < n and 0 <= cidx < m and board[ridx][cidx] == 1


def paint_island(ridx: int, cidx: int, island: int) -> None:
    que: deque[tuple[int, int]] = deque()

    que.append((ridx, cidx))
    board[ridx][cidx] = island

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in MOVE_LIST:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if is_connected(next_ridx, next_cidx):
                que.append((next_ridx, next_cidx))
                board[next_ridx][next_cidx] = island


def paint() -> int:
    island: int = 2
    for ridx, row in enumerate(board):
        for cidx, elem in enumerate(row):
            if elem == 1:
                paint_island(ridx, cidx, island)
                island += 1
    return island


def find_none_zero(row: list[int]) -> int:
    for idx, elem in enumerate(row):
        if elem != 0:
            return idx
    return -1


def link(row: list[int]) -> None:
    sidx = find_none_zero(row)
    if sidx == -1:
        return
    start: int = row[sidx]
    for idx, elem in enumerate(row):
        if elem == 0:
            continue
        elif elem == start:
            sidx = idx
        else:
            length: int = idx - sidx - 1
            if length > 1:
                bridge_list[start].append((length, elem))
                bridge_list[elem].append((length, start))
            sidx = idx
            start = elem


def connect(island: int) -> int:
    answer: int = 0
    connected: set[int] = set([2])
    candidates: list[tuple[int, int]] = []

    for length, elem in bridge_list[2]:
        heapq.heappush(candidates, (length, elem))

    while candidates:
        length, elem = heapq.heappop(candidates)
        if elem not in connected:
            connected.add(elem)
            answer += length
            for adj_length, adj_elem in bridge_list[elem]:
                if adj_elem not in connected:
                    heapq.heappush(candidates, (adj_length, adj_elem))

    return answer if len(connected) == island - 2 else -1


def main() -> None:
    global n, m, board, bridge_list
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    island = paint()

    bridge_list = [[] for _ in range(island)]
    for row in board:
        link(row)
    for col in zip(*board):
        link(list(col))

    print(connect(island))


if __name__ == "__main__":
    main()
