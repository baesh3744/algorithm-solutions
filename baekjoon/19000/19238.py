import sys
from collections import deque


moves: list[tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def find_passenger(taxi_ridx: int,
                   taxi_cidx: int) -> tuple[int, int, int, int]:
    if from_board[taxi_ridx][taxi_cidx] != 0:
        return from_board[taxi_ridx][taxi_cidx], taxi_ridx, taxi_cidx, 0

    go = True
    move = 0
    pas_num, pas_ridx, pas_cidx = 0, sys.maxsize, sys.maxsize
    que: deque[tuple[int, int]] = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]

    que.append((taxi_ridx, taxi_cidx))
    visited[taxi_ridx][taxi_cidx] = True

    while que and go:
        for _ in range(len(que)):
            cur_ridx, cur_cidx = que.popleft()

            for move_ridx, move_cidx in moves:
                next_ridx = cur_ridx + move_ridx
                next_cidx = cur_cidx + move_cidx

                if 0 <= next_ridx < n and 0 <= next_cidx < n \
                   and not visited[next_ridx][next_cidx] \
                   and board[next_ridx][next_cidx] == 0:
                    if from_board[next_ridx][next_cidx] != 0:
                        if next_ridx < pas_ridx \
                           or (next_ridx == pas_ridx and next_cidx < pas_cidx):
                            go = False
                            pas_num = from_board[next_ridx][next_cidx]
                            pas_ridx, pas_cidx = next_ridx, next_cidx
                    else:
                        que.append((next_ridx, next_cidx))
                        visited[next_ridx][next_cidx] = True
        move += 1

    if pas_num == 0:
        return -1, -1, -1, -1
    return pas_num, pas_ridx, pas_cidx, move


def move_to(pas_num: int,
            pas_ridx: int,
            pas_cidx: int) -> tuple[int, int, int]:
    goal_ridx, goal_cidx = to_board[pas_num]
    que: deque[tuple[int, int, int]] = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]

    que.append((pas_ridx, pas_cidx, 0))
    visited[pas_ridx][pas_cidx] = True

    while que:
        cur_ridx, cur_cidx, move = que.popleft()

        for move_ridx, move_cidx in moves:
            next_ridx = cur_ridx + move_ridx
            next_cidx = cur_cidx + move_cidx
            next_move = move + 1

            if 0 <= next_ridx < n and 0 <= next_cidx < n \
               and not visited[next_ridx][next_cidx] \
               and board[next_ridx][next_cidx] == 0:
                if next_ridx == goal_ridx and next_cidx == goal_cidx:
                    return next_ridx, next_cidx, next_move

                que.append((next_ridx, next_cidx, next_move))
                visited[next_ridx][next_cidx] = True

    return -1, -1, -1


def move(passenger: int,
         taxi_ridx: int,
         taxi_cidx: int,
         fuel: int) -> int:
    if passenger == 0:
        return fuel

    pas_num, pas_ridx, pas_cidx, pas_move \
        = find_passenger(taxi_ridx, taxi_cidx)
    if pas_move == -1 or pas_move > fuel:
        return -1
    fuel -= pas_move

    goal_ridx, goal_cidx, goal_move \
        = move_to(pas_num, pas_ridx, pas_cidx)
    if goal_move == -1 or goal_move > fuel:
        return -1
    fuel += goal_move

    from_board[pas_ridx][pas_cidx] = 0

    return move(passenger - 1, goal_ridx, goal_cidx, fuel)


def main() -> None:
    global n, board, from_board, to_board
    n, m, init_fuel = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]
    init_row, init_col = map(int, input().split())

    from_board = [[0 for _ in range(n)] for _ in range(n)]
    to_board = [[0, 0] for _ in range(m + 1)]
    for num in range(1, m + 1):
        from_row, from_col, to_row, to_col = map(int, input().split())
        from_board[from_row - 1][from_col - 1] = num
        to_board[num] = [to_row - 1, to_col - 1]

    print(move(m, init_row - 1, init_col - 1, init_fuel))


if __name__ == "__main__":
    main()
