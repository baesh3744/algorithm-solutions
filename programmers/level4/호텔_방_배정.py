import sys
from typing import Dict, List
sys.setrecursionlimit(10000000)


def find_empty_room(number: int, rooms: Dict[int, int]) -> int:
    if number not in rooms:
        rooms[number] = number + 1
        return number

    empty_room: int = find_empty_room(rooms[number], rooms)
    rooms[number] = empty_room + 1
    return empty_room


def solution(k: int, room_number: List[int]):
    answer: List[int] = []
    rooms: Dict[int, int] = {}

    for number in room_number:
        empty_room: int = find_empty_room(number, rooms)
        answer.append(empty_room)

    return answer


print(solution(10, [1, 3, 4, 1, 3, 1]))
print(solution(10, [10, 8, 8]))
print(solution(10, [2, 1, 2]))
print(solution(10, [1, 4, 3, 2]))
print(solution(10, [1, 4, 3, 3]))
