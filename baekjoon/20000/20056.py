import sys


Board = list[list[list[tuple[int, int, int]]]]

input = sys.stdin.readline

EMPTY: list[tuple[int, int, int]] = []
MOVE_RIDX: list[int] = [-1, -1, 0, 1, 1,  1,  0, -1]
MOVE_CIDX: list[int] = [0,   1, 1, 1, 0, -1, -1, -1]
NEW_DIRS: list[list[int]] = [
    [0, 2, 4, 6],
    [1, 3, 5, 7]
]

board: Board = [[[]]]


def move_fires(n: int) -> None:
    global board
    moved: Board = [[[] for _ in range(n)] for _ in range(n)]
    for ridx, row in enumerate(board):
        for cidx, fires in enumerate(row):
            for fire in fires:
                _, speed, dir = fire
                next_ridx = (ridx + speed*MOVE_RIDX[dir] + n) % n
                next_cidx = (cidx + speed*MOVE_CIDX[dir] + n) % n
                moved[next_ridx][next_cidx].append(fire)
    board = moved


def split_fires() -> None:
    for ridx, row in enumerate(board):
        for cidx, fires in enumerate(row):
            cnt_fire = len(fires)

            if cnt_fire <= 1:
                continue

            new_mass, new_speed, new_dir_type = 0, 0, 0
            for mass, speed, dir in fires:
                new_mass += mass
                new_speed += speed
                new_dir_type += dir % 2

            board[ridx][cidx] = EMPTY[:]

            if new_mass < 5:
                continue

            new_mass = new_mass // 5
            new_speed = new_speed // cnt_fire
            new_dir_type = 0 if new_dir_type in (0, cnt_fire) else 1
            for new_dir in NEW_DIRS[new_dir_type]:
                board[ridx][cidx].append((new_mass, new_speed, new_dir))


def get_total_mass() -> int:
    return sum([mass for row in board for fires in row
                for mass, _, _ in fires])


def order_k_times(n: int, k: int):
    for _ in range(k):
        move_fires(n)
        split_fires()
    return get_total_mass()


def main() -> None:
    global board
    n, m, k = map(int, input().split())

    board = [[[] for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        r, c, mass, speed, dir = map(int, input().split())
        board[r-1][c-1].append((mass, speed, dir))

    print(order_k_times(n, k))


if __name__ == "__main__":
    main()
