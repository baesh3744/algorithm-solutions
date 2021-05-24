move_x: list[int] = [1, 0, -1, 0]
move_y: list[int] = [0, -1, 0, 1]


def get_directions(init_direction: int, generation: int) -> list[int]:
    directions: list[int] = [init_direction]
    for _ in range(generation):
        for idx in range(len(directions) - 1, -1, -1):
            directions.append(directions[idx] - 1 if 0 < directions[idx]
                              else 3)
    return directions


def mark_dragon_curve(x: int, y: int, init_direciton: int, generation: int, board: list[list[bool]]) -> list[list[bool]]:
    directions = get_directions(init_direciton, generation)
    board[y][x] = True
    for idx, dir in enumerate(directions):
        if idx % 2 == 0:
            x += move_x[dir]
            y += move_y[dir]
        else:
            x -= move_x[dir]
            y -= move_y[dir]
        board[y][x] = True
    return board


def count_dragon_square(board: list[list[bool]]) -> int:
    cnt_square: int = 0
    for ridx in range(100):
        for cidx in range(100):
            if (board[ridx][cidx] and
                    board[ridx][cidx + 1] and
                    board[ridx + 1][cidx] and
                    board[ridx + 1][cidx + 1]):
                cnt_square += 1
    return cnt_square


def main() -> None:
    n = int(input())
    inputs = [list(map(int, input().split())) for _ in range(n)]

    board = [[False for _ in range(101)] for _ in range(101)]
    for x, y, direction, generation in inputs:
        board = mark_dragon_curve(x, y, direction, generation, board)
    print(count_dragon_square(board))


if __name__ == "__main__":
    main()
