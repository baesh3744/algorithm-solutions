from typing import List, Tuple


def solve(N: int, M: int, x: int, y: int, board: List[List[int]], cmds: List[int]) -> None:
    moves: List[Tuple[int, int]] = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]
    dice: List[int] = [0 for _ in range(6)]
    cur_x: int = x
    cur_y: int = y
    is_in: bool = False

    for cmd in cmds:
        if is_in:
            print(dice[0])

        move_x, move_y = moves[cmd]
        next_x: int = cur_x + move_x
        next_y: int = cur_y + move_y

        if 0 <= next_x < N and 0 <= next_y < M:
            is_in = True

            # 주사위 이동
            if cmd == 1:
                dice[0], dice[1], dice[4], dice[5] = dice[5], dice[4], dice[0], dice[1]
            elif cmd == 2:
                dice[0], dice[1], dice[4], dice[5] = dice[4], dice[5], dice[1], dice[0]
            elif cmd == 3:
                dice[0], dice[1], dice[2], dice[3] = dice[2], dice[3], dice[1], dice[0]
            else:
                dice[0], dice[1], dice[2], dice[3] = dice[3], dice[2], dice[0], dice[1]

            # 수 복사
            if board[next_x][next_y] == 0:
                board[next_x][next_y] = dice[1]
            else:
                dice[1] = board[next_x][next_y]
                board[next_x][next_y] = 0

            cur_x = next_x
            cur_y = next_y
        else:
            is_in = False

    if is_in:
        print(dice[0])


def main() -> None:
    N, M, x, y, _ = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    cmds = list(map(int, input().split()))

    solve(N, M, x, y, board, cmds)


if __name__ == "__main__":
    main()
