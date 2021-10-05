import sys
from collections import deque


Point = tuple[int, int]
Roads = list[list[set[Point]]]

MOVE_LIST: list[Point] = [(-1, 0), (0, -1), (1, 0), (0, 1)]

input = sys.stdin.readline


def make_group(n: int, roads: Roads, cows: list[list[bool]]) -> list[int]:
    group: list[int] = []
    visited: list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]

    for ridx in range(n):
        for cidx in range(n):
            if not visited[ridx][cidx]:
                cnt: int = 0
                que: deque[Point] = deque()

                if cows[ridx][cidx]:
                    cnt += 1
                que.append((ridx, cidx))
                visited[ridx][cidx] = True

                while que:
                    cur_ridx, cur_cidx = que.popleft()

                    for move_ridx, move_cidx in MOVE_LIST:
                        next_ridx: int = cur_ridx + move_ridx
                        next_cidx: int = cur_cidx + move_cidx

                        if (
                            0 <= next_ridx < n
                            and 0 <= next_cidx < n
                            and not visited[next_ridx][next_cidx]
                            and (next_ridx, next_cidx) not in roads[cur_ridx][cur_cidx]
                        ):
                            if cows[next_ridx][next_cidx]:
                                cnt += 1
                            que.append((next_ridx, next_cidx))
                            visited[next_ridx][next_cidx] = True

                group.append(cnt)

    return group


def count(k: int, group: list[int]) -> int:
    return sum(cow * (k - cow) for cow in group) // 2


def main() -> None:
    n, k, r = map(int, input().split())

    roads: Roads = [[set() for _ in range(n)] for _ in range(n)]
    for _ in range(r):
        r1, c1, r2, c2 = map(lambda x: int(x) - 1, input().split())
        roads[r1][c1] |= set([(r2, c2)])
        roads[r2][c2] |= set([(r1, c1)])

    cows: list[list[bool]] = [[False for _ in range(n)] for _ in range(n)]
    for _ in range(k):
        ridx, cidx = map(lambda x: int(x) - 1, input().split())
        cows[ridx][cidx] = True

    group = make_group(n, roads, cows)
    print(count(k, group))


if __name__ == "__main__":
    main()
