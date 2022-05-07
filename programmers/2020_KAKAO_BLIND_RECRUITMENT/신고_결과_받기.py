from collections import Counter
from typing import Dict, List


def solution(id_list: List[str], report: List[str], k: int) -> List[int]:
    report_set: set[str] = set(report)

    reported_counter: Counter[str] = Counter(map(lambda x: x.split()[1], report_set))
    stopped_ids = set(filter(lambda x: reported_counter[x] >= k, reported_counter))

    answer: List[int] = [0 for _ in range(len(id_list))]
    index_by_id: Dict[str, int] = {id: idx for idx, id in enumerate(id_list)}
    for reporter, reported in map(lambda x: x.split(), report_set):
        if reported in stopped_ids:
            answer[index_by_id[reporter]] += 1

    return answer


# [2,1,1,0]
print(
    solution(
        ["muzi", "frodo", "apeach", "neo"],
        ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
        2,
    )
)

# [0,0]
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
