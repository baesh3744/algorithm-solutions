from typing import List, Tuple
from collections import deque


def solve(N: int, has_apple: List[List[bool]], change_dirs: 'deque[Tuple[int, str]]') -> int:
    dirs: List[Tuple[int, int]] = [(0, 1), (-1, 0), (0, -1), (1, 0)]
    snake: 'deque[Tuple[int, int]]' = deque()
    time: int = 1
    didx: int = 0

    snake.append((0, 0))

    while True:
        prev_hridx, prev_hcidx = snake[-1]

        # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
        move_ridx, move_cidx = dirs[didx]
        hridx: int = prev_hridx + move_ridx
        hcidx: int = prev_hcidx + move_cidx
        snake.append((hridx, hcidx))

        # 벽과 부딪히면 게임이 끝난다.
        if not (0 <= hridx < N and 0 <= hcidx < N):
            return time

        # 자기자신과 부딪히면 게임이 끝난다.
        for idx in range(len(snake) - 1):
            if snake[idx] == snake[-1]:
                return time

        # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
        if has_apple[hridx][hcidx]:
            has_apple[hridx][hcidx] = False
        # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다.
        else:
            snake.popleft()

        # 방향을 바꿀 시간이 되면, 방향을 바꾼다. 시간이 1초 증가한다.
        if len(change_dirs) > 0 and change_dirs[0][0] == time:
            if change_dirs[0][1] == 'L':
                didx = didx + 1 if didx < 3 else 0
            else:
                didx = didx - 1 if didx > 0 else 3
            change_dirs.popleft()
        time += 1


def main() -> None:
    N = int(input())
    has_apple: List[List[bool]] = [[False for _ in range(N)] for _ in range(N)]
    K = int(input())
    for _ in range(K):
        ridx, cidx = map(int, input().split())
        has_apple[ridx - 1][cidx - 1] = True
    L = int(input())
    change_dirs: 'deque[Tuple[int, str]]' = deque()
    for _ in range(L):
        time, dir = input().split()
        change_dirs.append((int(time), dir))

    print(solve(N, has_apple, change_dirs))


if __name__ == "__main__":
    main()
