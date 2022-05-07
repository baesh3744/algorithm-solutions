from collections import defaultdict
from math import ceil
from typing import DefaultDict, List


def time2int(time: str) -> int:
    hour, minute = map(int, time.split(":"))
    return 60 * hour + minute


def calculate_time(records: List[str]) -> DefaultDict[str, int]:
    time_by_car: DefaultDict[str, int] = defaultdict(int)
    for time, car, type in map(lambda x: x.split(), records):
        if type == "IN":
            time_by_car[car] += 1439 - time2int(time)
        else:
            time_by_car[car] -= 1439 - time2int(time)
    return time_by_car


def calculate_fee(time: int, fees: List[int]) -> int:
    base_time, base_fee, per_time, per_fee = fees
    if time <= base_time:
        return base_fee
    return base_fee + ceil((time - base_time) / per_time) * per_fee


def solution(fees: List[int], records: List[str]) -> List[int]:
    answer: List[int] = []
    time_by_car = calculate_time(records)
    for _, time in sorted(time_by_car.items()):
        answer.append(calculate_fee(time, fees))
    return answer


# [14600, 34400, 5000]
print(
    solution(
        [180, 5000, 10, 600],
        [
            "05:34 5961 IN",
            "06:00 0000 IN",
            "06:34 0000 OUT",
            "07:59 5961 OUT",
            "07:59 0148 IN",
            "18:59 0000 IN",
            "19:09 0148 OUT",
            "22:59 5961 IN",
            "23:00 5961 OUT",
        ],
    )
)
# [0, 591]
print(
    solution(
        [120, 0, 60, 591],
        [
            "16:00 3961 IN",
            "16:00 0202 IN",
            "18:00 3961 OUT",
            "18:00 0202 OUT",
            "23:58 3961 IN",
        ],
    )
)
# [14841]
print(solution([1, 461, 1, 10], ["00:00 1234 IN"]))
