from typing import List, Tuple


def to_location(n: int, num: int) -> Tuple[int, int]:
    return num // n, num % n


def list_row(n: int, row: int) -> List[int]:
    return [row for _ in range(row)] + [num for num in range(row + 1, n + 1)]


def solution(n: int, left: int, right: int) -> List[int]:
    start_ridx, start_cidx = to_location(n, left)
    end_ridx, end_cidx = to_location(n, right)

    if start_ridx == end_ridx:
        return list_row(n, start_ridx + 1)[start_cidx : end_cidx + 1]

    answer: List[int] = []
    answer += list_row(n, start_ridx + 1)[start_cidx:]
    for ridx in range(start_ridx + 1, end_ridx):
        answer += list_row(n, ridx + 1)
    answer += list_row(n, end_ridx + 1)[: end_cidx + 1]
    return answer


# [3,2,2,3]
print(solution(3, 2, 5))
# [4,3,3,3,4,4,4,4]
print(solution(4, 7, 14))
# [1, 2]
print(solution(4, 0, 1))
# [1]
print(solution(4, 0, 0))
