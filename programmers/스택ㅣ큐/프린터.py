from typing import List


def solution(priorities: List[int], location: int) -> int:
    answer: int = 0
    prev: int = -1

    for priority in sorted(set(priorities), reverse=True):
        if priority < priorities[location]:
            break

        same_priorities = [idx for idx, pri in enumerate(priorities) if priority == pri]
        print_orders = list(filter(lambda x: x > prev, same_priorities)) + list(
            filter(lambda x: x < prev, same_priorities)
        )
        if location in print_orders:
            answer += print_orders.index(location) + 1
        else:
            answer += len(print_orders)

        prev = print_orders[-1]

    return answer


# 1
print(solution([2, 1, 3, 2], 2))
# 5
print(solution([1, 1, 9, 1, 1, 1], 0))
