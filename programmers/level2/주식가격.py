from typing import List, Tuple


def solution(prices: List[int]):
    answer = [time for time in range(len(prices)-1, -1, -1)]
    stack: List[Tuple[int, int]] = []

    for index, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            prev_index, _ = stack.pop()
            answer[prev_index] = index - prev_index
        stack.append((index, price))

    return answer


# [4, 3, 1, 1, 0]
print(solution([1, 2, 3, 2, 3]))
