import sys


IMP = sys.maxsize

input = sys.stdin.readline


def cover(ridx: int, cidx: int, size: int, adding: int) -> bool:
    can_cover: bool = True

    for _ridx in range(ridx, ridx + size):
        for _cidx in range(cidx, cidx + size):
            if board[_ridx][_cidx] != 1:
                can_cover = False
            board[_ridx][_cidx] += adding

    return can_cover


def count_paper() -> int:
    for ridx, row in enumerate(board):
        for cidx, elem in enumerate(row):
            if elem != 1:
                continue

            cnt: int = IMP

            for idx, paper in enumerate(paper_list):
                size: int = 5 - idx
                if paper == 0 or ridx + size > 10 or cidx + size > 10:
                    continue

                can_cover = cover(ridx, cidx, size, 2)
                if can_cover:
                    paper_list[idx] -= 1
                    cnt = min(cnt, 1 + count_paper())
                    paper_list[idx] += 1
                cover(ridx, cidx, size, -2)

            return cnt

    return 0


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(10)]

    paper_list: list[int] = [5, 5, 5, 5, 5]
    ans = count_paper()
    print(ans if ans != IMP else -1)
