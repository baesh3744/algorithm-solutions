from typing import Final, List, Tuple


TARGET: Final[str] = '110'
TRIPLE: Final[str] = '111'
ZERO: Final[str] = '0'


def remove_target(x: str) -> Tuple[str, int]:
    cnt: int = 0
    while (idx := x.find(TARGET)) != -1:
        x = x[:idx] + x[idx+3:]
        cnt += 1
    return x, cnt


def get_insert_pointer(x: str) -> int:
    pointer_triple: int = x.find(TRIPLE)
    pointer_zero: int = x.rfind(ZERO)

    if pointer_triple == -1 and pointer_zero == -1:
        return 0
    elif pointer_triple == -1 and pointer_zero != -1:
        return pointer_zero + 1
    elif pointer_triple != -1 and pointer_zero == -1:
        return pointer_triple
    else:
        return min(pointer_triple, pointer_zero + 1)


def update(x: str) -> str:
    removed_x, cnt = remove_target(x)
    pointer = get_insert_pointer(removed_x)

    updated_x = removed_x[:pointer] + TARGET * cnt + removed_x[pointer:]
    return updated_x


def solution(s: List[str]) -> List[str]:
    answer: List[str] = []

    for x in s:
        answer.append(update(x))

    return answer
