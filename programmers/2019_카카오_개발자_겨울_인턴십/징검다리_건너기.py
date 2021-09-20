from typing import List


def solution(stones: List[int], k: int):
    low: int = 0
    high: int = max(stones)

    while low <= high:
        mid: int = (low + high) // 2

        stones_tmp: List[int] = stones[:]
        for idx in range(len(stones_tmp)):
            stones_tmp[idx] -= mid

        cnt: int = 0
        is_possible: bool = True
        for stone in stones_tmp:
            if stone <= 0:
                cnt += 1
            else:
                cnt = 0

            if cnt >= k:
                is_possible = False
                break

        if is_possible:
            low = mid + 1
        else:
            high = mid - 1

    return low


print(solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3))
