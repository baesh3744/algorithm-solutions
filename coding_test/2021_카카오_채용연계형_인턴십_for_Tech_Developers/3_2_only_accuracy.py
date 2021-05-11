from bisect import bisect_left
from collections import deque
from typing import List


def solution(n: int, k: int, cmd: List[str]):
    answer: str = ''
    pointer_idx: int = k
    table: List[int] = [num for num in range(n)]
    deleted: deque[int] = deque()

    for act in cmd:
        if act[0] == 'U':
            pointer_idx -= int(act.split()[1])
        elif act[0] == 'D':
            pointer_idx += int(act.split()[1])
        elif act == 'C':
            prev_length: int = len(table)
            deleted.append(table[pointer_idx])
            del table[pointer_idx]
            if pointer_idx == prev_length - 1:
                pointer_idx -= 1
        elif act == 'Z':
            row: int = deleted.pop()
            insert_idx: int = bisect_left(table, row)
            table.insert(insert_idx, row)
            if insert_idx <= pointer_idx:
                pointer_idx += 1

    for num in range(n):
        answer += 'O' if num in table else 'X'

    return answer


print(solution(8, 2,
               ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]))
print(solution(8, 2,
               ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]))
print(solution(5, 1,
               ["D 2"]))
print(solution(5, 4,
               ["C"]))
