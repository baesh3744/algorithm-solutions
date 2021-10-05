import sys
from typing import Dict, List, Set


def solution(gems: List[str]) -> List[int]:
    jewels: Set[str] = set(gems)
    jlength: int = len(jewels)
    counter: Dict[str, int] = {jewel: 0 for jewel in jewels}
    bought: int = 0
    sidx: int = 0
    answer: List[int] = [0, sys.maxsize]

    for eidx, gem in enumerate(gems):
        counter[gem] += 1
        if counter[gem] == 1:
            bought += 1

        if bought == jlength:
            while counter[gems[sidx]] > 1:
                counter[gems[sidx]] -= 1
                sidx += 1
            if eidx - sidx < answer[1] - answer[0]:
                answer = [sidx + 1, eidx + 1]

    return answer


# [3, 7]
print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))
# [1, 3]
print(solution(["AA", "AB", "AC", "AA", "AC"]))
# [1, 1]
print(solution(["XYZ", "XYZ", "XYZ"]))
# [1, 5]
print(solution(["ZZZ", "YYY", "NNNN", "YYY", "BBB"]))
