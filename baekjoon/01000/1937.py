import sys


MOVES = [(-1, 0), (0, 1), (1, 0), (0, -1)]

input = sys.stdin.readline


def isrange(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < n and 0 <= cidx < n


def move(ridx: int, cidx: int) -> int:
    if cache[ridx][cidx] != -1:
        return cache[ridx][cidx]

    ret: int = 1

    for move_ridx, move_cidx in MOVES:
        next_ridx: int = ridx + move_ridx
        next_cidx: int = cidx + move_cidx

        if (
            isrange(next_ridx, next_cidx)
            and board[ridx][cidx] < board[next_ridx][next_cidx]
        ):
            ret = max(ret, 1 + move(next_ridx, next_cidx))

    cache[ridx][cidx] = ret
    return ret


if __name__ == "__main__":
    sys.setrecursionlimit(300000)

    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

    ans: int = 0
    cache = [[-1 for _ in range(n)] for _ in range(n)]
    for ridx in range(n):
        for cidx in range(n):
            ans = max(ans, move(ridx, cidx))
    print(ans)
