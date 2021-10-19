import heapq
import sys


MAX = sys.maxsize
MOVE_LIST = [(1, 0), (0, 1), (-1, 0), (0, -1)]

input = sys.stdin.readline


def solve(n: int, m: int, board: list[list[int]]) -> int:
    heap: list[tuple[int, int, int]] = []
    cache = [[MAX for _ in range(m)] for _ in range(n)]

    heapq.heappush(heap, (0, 0, 0))
    cache[0][0] = 0

    while heap:
        ridx, cidx, wall = heapq.heappop(heap)
        if cache[ridx][cidx] < wall:
            continue

        for move_ridx, move_cidx in MOVE_LIST:
            next_ridx, next_cidx = ridx + move_ridx, cidx + move_cidx
            if 0 <= next_ridx < n and 0 <= next_cidx < m:
                next_wall = wall + board[next_ridx][next_cidx]
                if next_wall < cache[next_ridx][next_cidx]:
                    heapq.heappush(heap, (next_ridx, next_cidx, next_wall))
                    cache[next_ridx][next_cidx] = next_wall

    return cache[n - 1][m - 1]


def main() -> None:
    m, n = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]

    print(solve(n, m, board))


if __name__ == "__main__":
    main()
