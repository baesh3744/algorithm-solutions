from collections import deque
from typing import Dict, List


def solution(n: int, k: int, cmd: List[str]):
    answer: str = ''
    pointer: int = k
    table: Dict[int, int] = dict()
    deleted: deque[int] = deque()

    for row in range(n):
        table[row] = row

    for act in cmd:
        if act[0] == 'U':
            keys: List[int] = sorted(list(table.keys()))
            pointer = keys[keys.index(pointer) - int(act.split()[1])]
        elif act[0] == 'D':
            keys: List[int] = sorted(list(table.keys()))
            pointer = keys[keys.index(pointer) + int(act.split()[1])]
        elif act == 'C':
            keys: List[int] = sorted(list(table.keys()))
            if keys[-1] == pointer:
                new_pointer: int = keys[-2]
            else:
                new_pointer: int = keys[keys.index(pointer) + 1]
            del table[pointer]
            deleted.append(pointer)
            pointer = new_pointer
        elif act == 'Z':
            row: int = deleted.pop()
            table[row] = row

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
print(solution(5, 4,
               ["C", "U 3", "C", "Z"]))
