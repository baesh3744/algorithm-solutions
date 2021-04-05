from typing import Deque, List, Tuple
from collections import deque


def is_range(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < N and 0 <= cidx < N


def mark(ridx: int, cidx: int, visited: List[List[bool]], colors: List[str]) -> List[List[bool]]:
    que: Deque[Tuple[int, int]] = deque()
    moves: List[Tuple[int, int]] = [(-1, 0), (0, 1), (1, 0), (0, -1)]

    que.append((ridx, cidx))
    visited[ridx][cidx] = True

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in moves:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if (is_range(next_ridx, next_cidx)
                    and not visited[next_ridx][next_cidx]
                    and img[next_ridx][next_cidx] in colors):
                que.append((next_ridx, next_cidx))
                visited[next_ridx][next_cidx] = True

    return visited


# 적록색약 x: type = 0
# 적록색약 o: type = 1
def count_area(type: int) -> int:
    area: int = 0
    visited: List[List[bool]] = [[False for _ in range(N)] for _ in range(N)]

    for ridx, row in enumerate(img):
        for cidx, _ in enumerate(row):
            if not visited[ridx][cidx]:
                # 파란색을 봤을 때
                if img[ridx][cidx] == 'B':
                    visited = mark(ridx, cidx, visited, ['B'])
                # 적록색약이 아닌 사람이 빨강, 초록을 봤을 때
                elif type == 0:
                    visited = mark(ridx, cidx, visited, [img[ridx][cidx]])
                # 적록색약인 사람이 빨강, 초록을 봤을 때
                else:
                    visited = mark(ridx, cidx, visited, ['R', 'G'])

                area += 1

    return area


def main() -> None:
    global N, img
    N = int(input())
    img = [[ch for ch in input()] for _ in range(N)]

    print(count_area(0), count_area(1))


if __name__ == "__main__":
    main()
