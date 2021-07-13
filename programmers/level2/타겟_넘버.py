from typing import List


def count(numbers: List[int], target: int, index: int, total: int) -> int:
    if index == length:
        return 1 if total == target else 0
    if cache[index][total] != -1:
        return cache[index][total]

    cache[index][total] \
        = count(numbers, target, index + 1, total + numbers[index]) + \
        count(numbers, target, index + 1, total - numbers[index])
    return cache[index][total]


def solution(numbers: List[int], target: int):
    global length, cache

    length = len(numbers)
    sum_numbers = sum(numbers)
    cache = [[-1 for _ in range(2 * (sum_numbers + 1))] for _ in range(length)]

    return count(numbers, target + sum_numbers, 0, sum_numbers)


# 5
print(solution([1, 1, 1, 1, 1], 3))
