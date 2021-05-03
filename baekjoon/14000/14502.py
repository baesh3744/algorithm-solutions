from collections import deque
from copy import deepcopy
from itertools import combinations
from typing import List, Tuple


def get_safe_zones(n: int, m: int, board: List[List[int]]) -> List[Tuple[int, int]]:
    safe_zones: List[Tuple[int, int]] = []
    for ridx in range(n):
        for cidx in range(m):
            if board[ridx][cidx] == 0:
                safe_zones.append((ridx, cidx))
    return safe_zones


def get_init_gas(n: int, m: int, board: List[List[int]]) -> 'deque[Tuple[int, int]]':
    gas: 'deque[Tuple[int, int]]' = deque()
    for ridx in range(n):
        for cidx in range(m):
            if board[ridx][cidx] == 2:
                gas.append((ridx, cidx))
    return gas


def get_spread_board(n: int, m: int, board: List[List[int]]) -> List[List[int]]:
    moves: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    gas: 'deque[Tuple[int, int]]' = get_init_gas(n, m, board)
    spread_board: List[List[int]] = deepcopy(board)

    while gas:
        cur_ridx, cur_cidx = gas.popleft()
        for move_ridx, move_cidx in moves:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx
            if (0 <= next_ridx < n and 0 <= next_cidx < m
                    and spread_board[next_ridx][next_cidx] == 0):
                gas.append((next_ridx, next_cidx))
                spread_board[next_ridx][next_cidx] = 2

    return spread_board


def get_max_safe_zone_size(n: int, m: int, board: List[List[int]]) -> int:
    size: int = 0
    safe_zones: List[Tuple[int, int]] = get_safe_zones(n, m, board)

    for safes in combinations(safe_zones, 3):
        for safe in safes:
            board[safe[0]][safe[1]] = 1

        spread_board: List[List[int]] = get_spread_board(n, m, board)
        size = max(size, len(get_safe_zones(n, m, spread_board)))

        for safe in safes:
            board[safe[0]][safe[1]] = 0

    return size


def main() -> None:
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    print(get_max_safe_zone_size(n, m, board))


if __name__ == "__main__":
    main()
