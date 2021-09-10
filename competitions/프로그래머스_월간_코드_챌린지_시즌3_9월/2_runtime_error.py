from typing import Dict, List, Tuple


MOVE_DIR: Dict[str, int] = {"S": 0, "L": 1, "R": -1}
MOVE_LIST: List[Tuple[int, int]] = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def add(grid: List[str], ridx: int, cidx: int, dir: int, cnt: int) -> int:
    index: int = ridx * col + cidx
    if checked[index][dir]:
        return cnt
    checked[index][dir] = True

    next_dir = (dir + MOVE_DIR[grid[ridx][cidx]]) % 4
    next_ridx = (ridx + MOVE_LIST[next_dir][0]) % row
    next_cidx = (cidx + MOVE_LIST[next_dir][1]) % col
    return add(grid, next_ridx, next_cidx, next_dir, cnt + 1)


def solution(grid: List[str]) -> List[int]:
    global checked, row, col
    row, col = len(grid), len(grid[0])
    length: int = row * col
    checked = [[False for _ in range(4)] for _ in range(length)]

    answer: List[int] = []
    for _grid in range(length):
        for dir in range(4):
            if not checked[_grid][dir]:
                answer.append(add(grid, _grid // col, _grid % col, dir, 0))
    return sorted(answer)


# [16]
print(solution(["SL", "LR"]))
# [1,1,1,1]
print(solution(["S"]))
# [4,4]
print(solution(["R", "R"]))
