from typing import List, Union

# attacked_map: 공격을 받은 후, 살아있으면 False, 죽으면 True


def make_attacked_map(n: int, map: List[List[int]], attack: Union[int, float]) -> List[List[bool]]:
    attacked_map: List[List[bool]] = [
        [False for _ in range(n)] for _ in range(n)]

    for ridx in range(n):
        for cidx in range(n):
            if float(map[ridx][cidx]) <= attack:
                attacked_map[ridx][cidx] = True
    return attacked_map


def make_range_map(r: int) -> List[List[int]]:
    range_map: List[List[int]] = [[0 for _ in range(r)] for _ in range(r)]

    for ridx in range(r):
        for cidx in range(r):
            if abs(ridx - cidx) < (r // 2) or


def count_died_monster(full_attacked_map: List[List[bool]],
                       half_attacked_map: List[List[bool]],
                       row: int,
                       col: int,
                       r: int) -> int:
    died_monster: int = 0

    attack_range: int = int(r / 2)

    for frange in range(attack_range):


def solution(maps: List[List[int]], p: int, r: int):
    answer = 10000
    n: int = len(maps)

    full_attacked_map: List[List[bool]] = make_attacked_map(n, maps, p)
    half_attacked_map: List[List[bool]] = make_attacked_map(n, maps, p / 2)

    for row in range(n + 1):
        for col in range(n + 1):
            answer = min(answer,
                         count_died_monster(full_attacked_map, half_attacked_map, row, col, r))

    return answer


print(solution([[1, 28, 41, 22, 25, 79, 4],
                [39, 20, 10, 17, 19, 18, 8],
                [21, 4, 13, 12, 9, 29, 19],
                [58, 1, 20, 5, 8, 16, 9],
                [5, 6, 15, 2, 39, 8, 29],
                [39, 7, 17, 5, 4, 49, 5],
                [74, 46, 8, 11, 25, 2, 11]],
               19, 6))  # 17
print(solution([[47, 8, 99, 9, 85, 3, 8],
                [90, 93, 8, 25, 98, 15, 97],
                [9, 95, 91, 87, 8, 81, 9],
                [98, 88, 82, 89, 79, 81, 97],
                [97, 35, 31, 97, 81, 2, 92],
                [32, 16, 49, 9, 91, 89, 17],
                [53, 6, 35, 12, 13, 98, 5]],
               78, 6))  # 11
print(solution([[9, 8, 17, 55, 19, 7],
                [1, 25, 5, 39, 28, 8],
                [88, 19, 28, 3, 2, 9],
                [76, 73, 7, 18, 16, 14],
                [99, 8, 8, 7, 11, 9],
                [1, 18, 4, 10, 3, 6]],
               16, 4))  # 8
print(solution([[6, 3, 2, 7, 3],
                [7, 2, 1, 6, 8],
                [8, 9, 8, 4, 9],
                [7, 9, 2, 7, 1],
                [6, 3, 6, 8, 4]],
               5, 2))  # 3
