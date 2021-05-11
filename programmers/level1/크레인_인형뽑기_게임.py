from collections import deque
from typing import List


def get_top_idxs(n: int, board: List[List[int]]) -> List[int]:
    cnt_update: int = 0
    top_idxs: List[int] = [n] * n

    for tidx in range(n):
        if cnt_update == n:
            break

        for idx in range(n):
            if top_idxs[idx] == n and board[tidx][idx] != 0:
                top_idxs[idx] = tidx
                cnt_update += 1

    return top_idxs


def solution(board: List[List[int]], moves: List[int]):
    answer: int = 0
    n: int = len(board)
    stack: deque[int] = deque()

    top_idxs: List[int] = get_top_idxs(n, board)

    for move in moves:
        if top_idxs[move - 1] == n:
            continue

        doll: int = board[top_idxs[move - 1]][move - 1]
        top_idxs[move - 1] += 1
        if len(stack) == 0 or doll != stack[-1]:
            stack.append(doll)
        else:
            stack.pop()
            answer += 2

    return answer


print(solution([[0, 0, 0, 0, 0],
                [0, 0, 1, 0, 3],
                [0, 2, 5, 0, 1],
                [4, 2, 4, 4, 2],
                [3, 5, 1, 3, 1]],
               [1, 5, 3, 5, 1, 2, 1, 4]))

# [[0, 0, 0, 0, 0],
#  [0, 0, 1, 0, 3],
#  [0, 2, 5, 0, 1],
#  [4, 2, 4, 4, 2],
#  [3, 5, 1, 3, 1]]

# 4 3 1 1 3 2 1
