from typing import Dict, List, Tuple


Loc = Tuple[int, int]
Queries = List[List[int]]

MOVE_RIDX: List[int] = [0, 0, -1, 1]
MOVE_CIDX: List[int] = [-1, 1, 0, 0]

cache: List[Dict[Loc, int]]


def to_inside(bound: int, idx: int) -> int:
    if idx < 0:
        return 0
    if idx > bound:
        return bound
    return idx


def get_next_location(n: int, m: int, loc: Loc, command: int, dx: int) -> Loc:
    next_ridx: int = loc[0] + dx * MOVE_RIDX[command]
    next_cidx: int = loc[1] + dx * MOVE_CIDX[command]
    return to_inside(n - 1, next_ridx), to_inside(m - 1, next_cidx)


def save(locations: List[Loc], res: int) -> None:
    for index, loc in enumerate(locations):
        cache[index][loc] = res


def move(n: int, m: int, x: int, y: int, queries: Queries, loc: Loc) -> int:
    ret: int = -1
    locations: List[Loc] = []
    for index, (command, dx) in enumerate(queries):
        loc = get_next_location(n, m, loc, command, dx)
        if loc in cache[index]:
            ret = cache[index][(loc)]
            break
        locations.append((loc))
    if ret == -1:
        ret = int(loc[0] == x and loc[1] == y)
    save(locations, ret)
    return ret


def solution(n: int, m: int, x: int, y: int, queries: Queries) -> int:
    global cache
    cache = [dict() for _ in range(len(queries))]

    answer: int = 0
    for ridx in range(n):
        for cidx in range(m):
            answer += move(n, m, x, y, queries, (ridx, cidx))
    return answer


# 4
print(solution(2, 2, 0, 0, [[2, 1], [0, 1], [1, 1], [0, 1], [2, 1]]))
# 2
print(solution(2, 5, 0, 1, [[3, 1], [2, 2], [1, 1], [2, 3], [0, 1], [2, 1]]))
