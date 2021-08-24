from collections import deque
from typing import Deque


def play(m: int, dodo: Deque[int], suyeon: Deque[int]) -> str:
    dodo_ground: Deque[int] = deque()
    suyeon_ground: Deque[int] = deque()

    for turn in range(m):
        if turn % 2 == 0:
            dodo_ground.append(dodo.pop())
            if not dodo:
                return "su"
        else:
            suyeon_ground.append(suyeon.pop())
            if not suyeon:
                return "do"

        if dodo_ground and suyeon_ground and dodo_ground[-1] + suyeon_ground[-1] == 5:
            while dodo_ground:
                suyeon.appendleft(dodo_ground.popleft())
            while suyeon_ground:
                suyeon.appendleft(suyeon_ground.popleft())
        elif (dodo_ground and dodo_ground[-1] == 5) or (
            suyeon_ground and suyeon_ground[-1] == 5
        ):
            while suyeon_ground:
                dodo.appendleft(suyeon_ground.popleft())
            while dodo_ground:
                dodo.appendleft(dodo_ground.popleft())

    cnt_dodo, cnt_suyeon = len(dodo), len(suyeon)
    if cnt_dodo == cnt_suyeon:
        return "dosu"
    if cnt_dodo > cnt_suyeon:
        return "do"
    return "su"


def main() -> None:
    n, m = map(int, input().split())

    dodo: Deque[int] = deque()
    suyeon: Deque[int] = deque()
    for _ in range(n):
        do, su = map(int, input().split())
        dodo.append(do)
        suyeon.append(su)

    print(play(m, dodo, suyeon))


if __name__ == "__main__":
    main()
