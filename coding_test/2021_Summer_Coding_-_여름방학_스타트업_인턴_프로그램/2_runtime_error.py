from typing import List, Tuple


def get_first_person(waiting: dict[int, Tuple[int, int]]) -> int:
    min_idx: int = 10000
    min_time: int = 100000
    min_rating: int = 10

    for key, value in waiting.items():
        if ((value[1] < min_rating)
            or (value[1] == min_rating and value[0] < min_time)
                or (value[1] == min_rating and value[0] == min_time and key < min_idx)):
            min_idx = key
            min_time = value[0]
            min_rating = value[1]

    return min_idx


def solution(t: List[int], r: List[int]) -> List[int]:
    answer: List[int] = []
    length: int = len(t)

    data: List[Tuple[int, int, int]] = [
        (t[idx], r[idx], idx) for idx in range(length)]
    data.sort()

    currrent: int = 0
    idx: int = 0
    waiting: dict[int, Tuple[int, int]] = {}

    while idx < length:
        while idx < length and data[idx][0] == currrent:
            waiting[data[idx][2]] = (data[idx][0], data[idx][1])
            idx += 1

        if waiting:
            first: int = get_first_person(waiting)
            del waiting[first]
            answer.append(first)
        currrent += 1

    while waiting:
        first: int = get_first_person(waiting)
        del waiting[first]
        answer.append(first)

    return answer


print(solution([0, 1, 3, 0], [0, 1, 2, 3]))  # [0, 1, 3, 2]
print(solution([7, 6, 8, 1], [0, 1, 2, 3]))  # [3, 1, 0, 2]
