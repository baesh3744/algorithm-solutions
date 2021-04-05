from typing import List
from queue import Queue


def get_next(M: int, cur: int, move: int) -> int:
    next: int = cur
    while board[next // M][next % M] == '.':
        next += move

    # 벽을 마주쳤을 때
    if board[next // M][next % M] == '#':
        return next - move
    # 구멍에 빠졌을 때
    return -1


def solve(N: int, M: int) -> int:
    red: int = -1
    blue: int = -1
    que: 'Queue[List[int]]' = Queue()
    visited: List[List[bool]] = [
        [False for _ in range(N * M)] for _ in range(N * M)]

    # 구슬의 처음 위치 찾기
    for i in range(1, N):
        for j in range(1, M):
            if board[i][j] == 'R':
                red = i * M + j
                board[i][j] = '.'
            elif board[i][j] == 'B':
                blue = i * M + j
                board[i][j] = '.'

    # 구슬의 처음 위치를 queue에 저장
    que.put([red, blue, 0])
    visited[red][blue] = True

    while not que.empty():
        red, blue, count = que.get()
        for midx, move in enumerate(moves):
            # 파란 구슬 이동. 파란 구슬이 빠지면 실패
            next_blue = get_next(M, blue, move)
            if next_blue == -1:
                continue

            # 빨간 구슬 이동. 빨간 구슬이 빠지면 성공
            next_red = get_next(M, red, move)
            if next_red == -1:
                return count + 1

            # 이동 후, 파란 구슬과 빨간 구슬이 같은 위치
            # 이동 전 위치를 통해 한 칸 덜 이동하는 구슬을 결정
            if next_red == next_blue:
                rrow: int = red // M
                brow: int = blue // M
                rcol: int = red % M
                bcol: int = blue % M

                if (midx == 0 and rrow < brow
                        or midx == 1 and rcol > bcol
                        or midx == 2 and rrow > brow
                        or midx == 3 and rcol < bcol):
                    next_blue -= move
                else:
                    next_red -= move

            # 이동 후 위치를 queue에 저장
            if not visited[next_red][next_blue]:
                que.put([next_red, next_blue, count + 1])
                visited[next_red][next_blue] = True

    # queue가 빌 때까지 성공하지 못하면, 실패
    return -1


def main() -> None:
    global board, moves
    N, M = map(int, input().split())
    board = [[ch for ch in input()] for _ in range(N)]

    moves = [-1 * M, 1, M, -1]

    print(solve(N, M))


if __name__ == "__main__":
    main()
