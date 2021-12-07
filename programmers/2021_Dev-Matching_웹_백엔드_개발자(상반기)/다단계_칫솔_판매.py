from collections import defaultdict
from typing import DefaultDict, List


def solution(
    enroll: List[str], referral: List[str], seller: List[str], amount: List[int]
) -> List[int]:
    benefits: DefaultDict[str, List[int]] = defaultdict(list)

    for slr, amt in zip(seller, amount):
        benefits[slr].append(amt * 100)

    length: int = len(enroll)
    result: List[int] = [0 for _ in range(length)]
    for idx in range(length - 1, -1, -1):
        en: str = enroll[idx]
        for benefit in benefits[en]:
            to_referral: int = benefit // 10
            result[idx] += benefit - to_referral
            if to_referral != 0:
                benefits[referral[idx]].append(to_referral)

    return result


# [360, 958, 108, 0, 450, 18, 180, 1080]
print(
    solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["young", "john", "tod", "emily", "mary"],
        [12, 4, 2, 5, 10],
    )
)
# [0, 110, 378, 180, 270, 450, 0, 0]
print(
    solution(
        ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"],
        ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"],
        ["sam", "emily", "jaimie", "edward"],
        [2, 3, 5, 4],
    )
)
