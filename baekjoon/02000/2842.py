import sys
from collections import deque


TVillage = list[list[str]]
THeights = list[list[int]]
TPoint = tuple[int, int]


def get_height_values(n: int,
                      village: TVillage,
                      heights: THeights) -> tuple[list[int], int, int, int]:
    height_values: set[int] = set()
    start_ridx: int = -1
    start_cidx: int = -1
    cnt_house: int = 0

    for ridx in range(n):
        for cidx in range(n):
            height_values.add(heights[ridx][cidx])
            if village[ridx][cidx] == 'P':
                start_ridx, start_cidx = ridx, cidx
            if village[ridx][cidx] == 'K':
                cnt_house += 1

    return sorted(height_values), start_ridx, start_cidx, cnt_house


def visit(n: int,
          village: TVillage,
          heights: THeights,
          start_ridx: int, start_cidx: int,
          min_height: int, max_height: int) -> int:
    moves: list[TPoint] = [(-1, -1), (-1, 0), (-1, 1),
                           (0, -1), (0, 1),
                           (1, -1), (1, 0), (1, 1)]
    cnt_visited: int = 0
    que: deque[TPoint] = deque()
    visited = [[False for _ in range(n)] for _ in range(n)]

    if min_height <= heights[start_ridx][start_cidx] <= max_height:
        que.append((start_ridx, start_cidx))
        visited[start_ridx][start_cidx] = True

    while que:
        cur_ridx, cur_cidx = que.popleft()

        for move_ridx, move_cidx in moves:
            next_ridx: int = cur_ridx + move_ridx
            next_cidx: int = cur_cidx + move_cidx

            if 0 <= next_ridx < n and \
                    0 <= next_cidx < n and \
                    not visited[next_ridx][next_cidx] and \
                    min_height <= heights[next_ridx][next_cidx] <= max_height:
                que.append((next_ridx, next_cidx))
                visited[next_ridx][next_cidx] = True
                if village[next_ridx][next_cidx] == 'K':
                    cnt_visited += 1

    return cnt_visited


def get_min_fatigue(n: int, village: TVillage, heights: THeights) -> int:
    height_values, start_ridx, start_cidx, cnt_house \
        = get_height_values(n, village, heights)

    left: int = 0
    right: int = 0
    length: int = len(height_values)
    min_diff: int = sys.maxsize

    while left <= right and left < length:
        left_height: int = height_values[left]
        right_height: int = height_values[right]

        cnt_visited = visit(n,
                            village,
                            heights,
                            start_ridx, start_cidx,
                            left_height, right_height)

        if cnt_visited == cnt_house:
            min_diff = min(min_diff, right_height - left_height)
            left += 1
        elif right + 1 < length:
            right += 1
        else:
            break

    return min_diff


def main() -> None:
    n = int(input())
    village = [list(input()) for _ in range(n)]
    heights = [list(map(int, input().split())) for _ in range(n)]

    print(get_min_fatigue(n, village, heights))


if __name__ == "__main__":
    main()
