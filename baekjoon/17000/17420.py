import sys
from collections import defaultdict
from math import ceil


PERIOD = 30

input = sys.stdin.readline


def group_by_plan() -> list[tuple[int, list[int]]]:
    plan_remaining_dict: defaultdict[int, list[int]] = defaultdict(list)
    for remaining, plan in zip(a, b):
        plan_remaining_dict[plan].append(remaining)
    return sorted(plan_remaining_dict.items())


def count() -> int:
    prev_max: int = 0
    time: int = 0
    for plan, remaining_list in grouped:
        min_bound: int = max(prev_max, plan)
        for remaining in remaining_list:
            if remaining < min_bound:
                cnt: int = ceil((min_bound - remaining) / PERIOD)
                remaining += cnt * PERIOD
                time += cnt
            prev_max = max(prev_max, remaining)
    return time


if __name__ == "__main__":
    n = int(input())
    a = map(int, input().split())
    b = map(int, input().split())

    grouped = group_by_plan()
    print(count())
