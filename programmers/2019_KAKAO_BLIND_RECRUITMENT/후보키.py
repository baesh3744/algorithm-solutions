from itertools import combinations
from typing import List, Set


def solution(relation: List[List[str]]):
    row, col = len(relation), len(relation[0])
    answer: List[Set[int]] = []

    for length in range(1, col + 1):
        for cbnt in combinations(range(col), length):
            unique = set(
                [tuple(relation[ridx][cidx] for cidx in cbnt) for ridx in range(row)]
            )

            if len(unique) != row:
                continue

            cbntset = set(cbnt)
            is_subset = False
            for ans in answer:
                if ans.issubset(cbntset):
                    is_subset = True
                    break
            if not is_subset:
                answer.append(cbntset)

    return len(answer)


# 2
print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)
