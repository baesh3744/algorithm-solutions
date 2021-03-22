from collections import deque
from typing import Deque


def count_zero(A: Deque[int]) -> int:
    count: int = 0
    for a in A:
        if a == 0:
            count += 1
    return count


def solve(A: Deque[int], robots: Deque[bool], N: int, K: int) -> None:
    step: int = 1
    while(True):
        # 1. 벨트가 한 칸 회전한다.
        A.rotate(1)
        robots.rotate(1)
        robots[N - 1] = False

        # 2. 가장 먼저 벨트에 올라간 로봇부터, 벨트가 회전하는 방향으로 한 칸 이동할 수 있다면 이동한다. 만약 이동할 수 없다면 가만히 있는다.
        # 로봇이 이동하기 위해서는 이동하려는 칸에 로봇이 없으며, 그 칸의 내구도가 1 이상 남아 있어야 한다.
        for index, robot in reversed(list(enumerate(robots))):
            if index == N - 1:
                continue

            if robot and not robots[index + 1] and A[index + 1] >= 1:
                robots[index] = False
                robots[index + 1] = True
                A[index + 1] -= 1
        robots[N - 1] = False

        # 3. 올라가는 위치에 로봇이 없다면 로봇을 하나 올린다.
        if not robots[0] and A[0] >= 1:
            robots[0] = True
            A[0] -= 1

        # 4. 내구도가 0인 칸의 개수가 K개 이상이라면 과정을 종료한다. 그렇지 않다면 1번으로 돌아간다.
        if count_zero(A) >= K:
            print(step)
            break
        else:
            step += 1


def main() -> None:
    N, K = map(int, input().split())
    A = deque(map(int, input().split()))
    robots = deque([False for _ in range(N)])
    solve(A, robots, N, K)


if __name__ == "__main__":
    main()
