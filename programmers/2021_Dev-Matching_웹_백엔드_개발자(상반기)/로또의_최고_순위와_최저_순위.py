from typing import List


TO_RANKING: List[int] = [6, 6, 5, 4, 3, 2, 1]


def solution(lottos: List[int], win_nums: List[int]) -> List[int]:
    common: int = len(set(lottos) & set(win_nums))
    return [TO_RANKING[common + lottos.count(0)], TO_RANKING[common]]


# [3, 5]
print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
# [1, 6]
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
# [1, 1]
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))
