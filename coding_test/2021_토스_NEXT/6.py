from typing import List


def solution(numOfStairs: int) -> int:
    cache: List[int] = [0, 1, 2, 4] + [-1 for _ in range(numOfStairs)]
    for stair in range(4, numOfStairs + 1):
        cache[stair] = cache[stair - 1] + cache[stair - 2] + cache[stair - 3]
    return cache[numOfStairs]


for n in range(1, 71):
    print(solution(n))
