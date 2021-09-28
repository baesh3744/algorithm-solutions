from typing import List, Set, Tuple


def solution(n: int, weak: List[int], dist: List[int]) -> int:
    friend: int = 0
    wlen: int = len(weak)
    repair_list: Set[Tuple[int, ...]] = set([()])

    dist.sort(reverse=True)

    for can_move in dist:
        friend += 1

        repairs: List[Set[int]] = []
        for idx, weak_point in enumerate(weak):
            ends: List[int] = weak[idx:] + [n + wp for wp in weak[:idx]]
            can: List[int] = [end % n for end in ends if end - weak_point <= can_move]
            repairs.append(set(can))

        cand: Set[Tuple[int, ...]] = set()
        for rp in repairs:
            for existing in repair_list:
                new: Set[int] = set(existing) | rp
                if len(new) == wlen:
                    return friend
                cand.add(tuple(new))
        repair_list = cand

    return -1


# Reference
# https://daewonyoon.tistory.com/363


# 2
print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
# 1
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
