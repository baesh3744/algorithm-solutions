from math import ceil, sqrt


def count_measures(num: int) -> int:
    cnt: int = 0
    for i in range(1, ceil(sqrt(num)) + 1):
        if num % i == 0:
            cnt += 2 if i ** 2 != num else 1
    return cnt


def solution(left: int, right: int):
    answer = 0

    for num in range(left, right + 1):
        if count_measures(num) % 2 == 0:
            answer += num
        else:
            answer -= num

    return answer


print(solution(13, 17))  # 43
print(solution(24, 27))  # 52
