from collections import deque
from typing import List

que: 'deque[List[List[int]]]' = deque()


def slant_row(N: int, row: List[int]) -> List[int]:
    slanted: List[int] = [0 for _ in range(N)]
    sidx: int = 0
    prev: int = -1

    for idx in range(0, N):
        if row[idx] == 0:
            continue

        if prev == -1:
            prev = row[idx]
        else:
            if prev != row[idx]:
                slanted[sidx] = prev
                prev = row[idx]
            else:
                slanted[sidx] = 2 * prev
                prev = -1
            sidx += 1
    if prev != -1:
        slanted[sidx] = prev

    return slanted


def slant_board(N: int, init_board: List[List[int]]) -> None:
    que.append(init_board)

    for cnt in range(5):
        for _ in range(4 ** cnt):
            cboard: List[List[int]] = que.popleft()

            # 좌
            nboard: List[List[int]] = []
            for idx in range(N):
                nboard.append(slant_row(N, cboard[idx]))
            que.append(nboard)

            # 우
            nboard = []
            for idx in range(N):
                reversed_row: List[int] = list(reversed(cboard[idx]))
                reversed_slanted = list(reversed(slant_row(N, reversed_row)))
                nboard.append(reversed_slanted)
            que.append(nboard)

            # 상
            nboard = []
            for idx in range(N):
                col: List[int] = [cboard[ridx][idx] for ridx in range(N)]
                nboard.append(slant_row(N, col))
            que.append(nboard)

            # 하
            nboard = []
            for idx in range(N):
                col: List[int] = [cboard[ridx][idx] for ridx in range(N)]
                reversed_col: List[int] = list(reversed(col))
                reversed_slanted = list(reversed(slant_row(N, reversed_col)))
                nboard.append(reversed_slanted)
            que.append(nboard)


def get_max_block(N: int) -> int:
    max_block: int = 0

    while que:
        board: List[List[int]] = que.popleft()

        for ridx in range(N):
            for cidx in range(N):
                max_block = max(max_block, board[ridx][cidx])

    return max_block


def main() -> None:
    N = int(input())
    init_board = [list(map(int, input().split())) for _ in range(N)]

    slant_board(N, init_board)
    print(get_max_block(N))


if __name__ == "__main__":
    main()
