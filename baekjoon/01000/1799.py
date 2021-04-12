from typing import List

r2l_node: List[int]
l2r_node: List[int]
link: List[List[int]]


def dfs(idx: int) -> bool:
    visited[idx] = True

    for l2r in link[idx]:
        if l2r_node[l2r] == -1 or (not visited[l2r_node[l2r]] and dfs(l2r_node[l2r])):
            r2l_node[idx] = l2r
            l2r_node[l2r] = idx
            return True
    return False


def initialize() -> None:
    global r2l_node, l2r_node, link
    msize: int = 2 * bsize
    r2l_node = [-1 for _ in range(msize)]
    l2r_node = [-1 for _ in range(msize)]
    link = [[] for _ in range(msize)]

    for ridx in range(bsize):
        for cidx in range(bsize):
            if board[ridx][cidx] == 1:
                link[ridx + cidx].append(bsize + ridx - cidx)


def main() -> None:
    global bsize, board, visited
    bsize = int(input())
    board = [list(map(int, input().split())) for _ in range(bsize)]

    initialize()

    ans: int = 0
    for idx, matching in enumerate(r2l_node):
        if matching == -1:
            visited = [False for _ in range(2 * bsize)]

            if dfs(idx):
                ans += 1

    print(ans)


if __name__ == "__main__":
    main()
