import sys


input = sys.stdin.readline


def dfs(ridx: int, cidx: int) -> bool:
    visited[ridx][cidx] = True

    if cidx == c - 1:
        return True

    for next_ridx in range(ridx - 1, ridx + 2):
        if (
            0 <= next_ridx < r
            and not visited[next_ridx][cidx + 1]
            and dfs(next_ridx, cidx + 1)
        ):
            return True

    return False


if __name__ == "__main__":
    r, c = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]

    visited = [[board[ridx][cidx] == "x" for cidx in range(c)] for ridx in range(r)]
    print(sum(int(dfs(ridx, 0)) for ridx in range(r)))
