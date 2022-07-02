import sys
from heapq import heappop, heappush


MAX = sys.maxsize
MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]
input = sys.stdin.readline


def is_range(n: int, m: int, row: int, column: int) -> bool:
    return 0 <= row < n and 0 <= column < m


def get_shortest_path(n: int, m: int, board: list[list[int]]) -> int:
    """벽을 최대 한 개까지 부수면서
    맵의 (0, 0)에서 (n-1, m-1)까지 이동할 수 있는 최단 경로의 길이를 구합니다.

    Args:
        n (int): 행 개수
        m (int): 열 개수
        board (list[list[int]]): 맵

    Returns:
        int: 경로의 길이. 경로가 존재하지 않을 때는 -1
    """

    if n == 1 and m == 1:
        return 1

    # 0 - 벽을 부술 수 없음. 1 - 벽을 부술 수 있음
    # heap: (경로의 길이, 행, 열, 벽을 부술 수 있는지)
    heap: list[tuple[int, int, int, int]] = []
    # cache[행][열][벽을 부술 수 있는지]: 경로의 길이
    cache = [[[MAX for _ in range(2)] for _ in range(m)] for _ in range(n)]

    heappush(heap, (1, 0, 0, 1))
    cache[0][0][1] = 1

    while heap:
        path, row, column, can_break = heappop(heap)

        if cache[row][column][can_break] < path:
            continue

        for move_row, move_column in MOVES:
            next_row, next_column = row + move_row, column + move_column
            next_can_break = can_break
            next_path = path + 1

            if not is_range(n, m, next_row, next_column):
                continue

            if board[next_row][next_column] == 1:
                if can_break == 0:
                    continue
                else:
                    next_can_break = 0

            if next_path < cache[next_row][next_column][next_can_break]:
                if next_row == n - 1 and next_column == m - 1:
                    return next_path

                heappush(heap, (next_path, next_row, next_column, next_can_break))
                cache[next_row][next_column][next_can_break] = next_path

    return -1


def main() -> None:
    n, m = map(int, input().split())
    board = [list(map(int, input().strip())) for _ in range(n)]

    print(get_shortest_path(n, m, board))


if __name__ == "__main__":
    main()
