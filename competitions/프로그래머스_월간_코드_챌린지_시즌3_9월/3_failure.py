from math import ceil
from typing import List


def solution(
    a: int, b: int, g: List[int], s: List[int], w: List[int], t: List[int]
) -> int:
    rate = sorted((_w / _t, index) for index, (_w, _t) in enumerate(zip(w, t)))

    index: int = 0
    answer: int = 0
    while a > 0 or b > 0:
        city: int = rate[index][1]

        gold_weight: int = min(a, g[city])
        silver_weight: int = min(b, s[city])
        a -= gold_weight
        b -= silver_weight

        move = ceil((gold_weight + silver_weight) / w[city])
        answer = max(answer, (2 * move - 1) * t[city])

        index += 1

    return answer


# 50
print(solution(10, 10, [100], [100], [7], [10]))
# 499
print(solution(90, 500, [70, 70, 0], [0, 0, 500], [100, 100, 2], [4, 8, 1]))
