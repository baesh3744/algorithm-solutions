import sys


Board = list[list[int]]
Cloud = set[tuple[int, int]]

CLOUD_MOVE_ROW: list[int] = [0, 0, -1, -1, -1, 0, 1, 1, 1]
CLOUD_MOVE_COL: list[int] = [0, -1, -1, 0, 1, 1, 1, 0, -1]
MOVES: list[tuple[int, int]] = [(-1, -1), (-1, 1), (1, -1), (1, 1)]


input = sys.stdin.readline


def move_cloud(n: int, d: int, s: int, cloud: Cloud) -> Cloud:
    return set(
        ((ridx + s * CLOUD_MOVE_ROW[d] + n) % n, (cidx + s * CLOUD_MOVE_COL[d] + n) % n)
        for ridx, cidx in cloud
    )


def copy_water(n: int, board: Board, cloud: Cloud) -> Board:
    for ridx, cidx in cloud:
        for move_ridx, move_cidx in MOVES:
            sur_ridx: int = ridx + move_ridx
            sur_cidx: int = cidx + move_cidx
            if 0 <= sur_ridx < n and 0 <= sur_cidx < n:
                board[ridx][cidx] += int(board[sur_ridx][sur_cidx] > 0)
    return board


def get_cloud(board: Board, existing_cloud: Cloud) -> tuple[Board, Cloud]:
    cloud: Cloud = set()
    for ridx, row in enumerate(board):
        for cidx, water in enumerate(row):
            if water >= 2 and (ridx, cidx) not in existing_cloud:
                board[ridx][cidx] -= 2
                cloud.add((ridx, cidx))
    return board, cloud


def move(n: int, d: int, s: int, board: Board, cloud: Cloud) -> tuple[Board, Cloud]:
    moved_cloud = move_cloud(n, d, s, cloud)
    for ridx, cidx in moved_cloud:
        board[ridx][cidx] += 1
    board = copy_water(n, board, moved_cloud)
    board, cloud = get_cloud(board, moved_cloud)
    return board, cloud


def sum_water(board: Board) -> int:
    return sum(sum(row) for row in board)


def main() -> None:
    n, m = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(n)]
    cloud = set([(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)])
    for _ in range(m):
        d, s = map(int, input().split())
        board, cloud = move(n, d, s, board, cloud)
    print(sum_water(board))


if __name__ == "__main__":
    main()
