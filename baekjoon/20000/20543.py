import sys


input = sys.stdin.readline


def solve() -> list[list[int]]:
    empty: int = m // 2
    ans: list[list[int]] = [[0 for _ in range(n)] for _ in range(n)]

    for ridx in range(empty, n - empty):
        for cidx in range(empty, n - empty):
            ans[ridx][cidx] = -board[ridx - empty][cidx - empty]
            if ridx - 1 >= empty:
                ans[ridx][cidx] += board[ridx - empty - 1][cidx - empty]
            if cidx - 1 >= empty:
                ans[ridx][cidx] += board[ridx - empty][cidx - empty - 1]
            if ridx - 1 >= empty and cidx - 1 >= empty:
                ans[ridx][cidx] += -board[ridx - empty - 1][cidx - empty - 1]
            if ridx - m >= empty:
                ans[ridx][cidx] += ans[ridx - m][cidx]
            if cidx - m >= empty:
                ans[ridx][cidx] += ans[ridx][cidx - m]
            if ridx - m >= empty and cidx - m >= empty:
                ans[ridx][cidx] += -ans[ridx - m][cidx - m]

    return ans


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    ans = solve()
    for row in ans:
        print(" ".join(map(str, row)))
