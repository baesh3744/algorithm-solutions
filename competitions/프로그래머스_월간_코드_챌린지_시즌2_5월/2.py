from typing import List


def get_change_bit(num: int) -> int:
    change_bit: int = 0

    while num > 0:
        if num & 1 == 0:
            return change_bit
        change_bit += 1
        num >>= 1

    return change_bit


def solution(numbers: List[int]):
    answer: List[int] = []

    for num in numbers:
        change_bit = get_change_bit(num)
        if change_bit == 0:
            answer.append(num + 2 ** change_bit)
        else:
            answer.append(num + 2 ** (change_bit - 1))

    return answer


print(solution([2, 7]))
# [3, 11]
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
# [2, 3, 5, 5, 6, 7, 11, 9, 10, 11]
