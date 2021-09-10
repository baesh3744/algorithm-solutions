from typing import List


def solution(numbers: List[int]) -> int:
    return 45 - sum(numbers)


# 14
print(solution([1, 2, 3, 4, 6, 7, 8, 0]))
# 6
print(solution([5, 8, 4, 0, 6, 7, 9]))
