from typing import List


MOVES = [(0, 1), (1, 0), (0, -1), (-1, 0)]
NEXT_DIRS = {"S": [0, 1, 2, 3], "L": [3, 0, 1, 2], "R": [1, 2, 3, 0]}


def move(ridx: int, cidx: int, dir: int, grid: List[str]) -> int:
    cycle: int = 0

    while not checked[ridx][cidx][dir]:
        cycle += 1
        checked[ridx][cidx][dir] = True

        move_ridx, move_cidx = MOVES[dir]
        ridx = (ridx + move_ridx) % row
        cidx = (cidx + move_cidx) % col
        dir = NEXT_DIRS[grid[ridx][cidx]][dir]

    return cycle


def solution(grid: List[str]) -> List[int]:
    global row, col, checked
    row, col = len(grid), len(grid[0])
    checked = [[[False for _ in range(4)] for _ in range(col)] for _ in range(row)]

    answer: List[int] = []
    for ridx in range(row):
        for cidx in range(col):
            for dir in range(4):
                if not checked[ridx][cidx][dir]:
                    answer.append(move(ridx, cidx, dir, grid))

    return sorted(answer)


# [16]
print(solution(["SL", "LR"]))
# [1,1,1,1]
print(solution(["S"]))
# [4,4]
print(solution(["R", "R"]))
