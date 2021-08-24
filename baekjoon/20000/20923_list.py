import sys
from typing import List


input = sys.stdin.readline


def play(n: int, m: int, dodo: List[int], suyeon: List[int]) -> str:
    cnt_dodo, cnt_suyeon = n, n
    ptr_dodo, ptr_suyeon = 0, 0
    dodo_ground: List[int] = []
    suyeon_ground: List[int] = []

    for turn in range(m):
        if turn % 2 == 0:
            dodo_ground.append(dodo[ptr_dodo])
            ptr_dodo += 1
            cnt_dodo -= 1
            if cnt_dodo == 0:
                return "su"
        else:
            suyeon_ground.append(suyeon[ptr_suyeon])
            ptr_suyeon += 1
            cnt_suyeon -= 1
            if cnt_suyeon == 0:
                return "do"

        if dodo_ground and suyeon_ground and dodo_ground[-1] + suyeon_ground[-1] == 5:
            suyeon += dodo_ground + suyeon_ground
            cnt_suyeon = 2 * n - cnt_dodo
            dodo_ground, suyeon_ground = [], []
        elif (dodo_ground and dodo_ground[-1] == 5) or (
            suyeon_ground and suyeon_ground[-1] == 5
        ):
            dodo += suyeon_ground + dodo_ground
            cnt_dodo = 2 * n - cnt_suyeon
            dodo_ground, suyeon_ground = [], []

    if cnt_dodo == cnt_suyeon:
        return "dosu"
    if cnt_dodo > cnt_suyeon:
        return "do"
    return "su"


def main() -> None:
    n, m = map(int, input().split())

    dodo: List[int] = [-1 for _ in range(n)]
    suyeon: List[int] = [-1 for _ in range(n)]
    for index in range(n - 1, -1, -1):
        do, su = map(int, input().split())
        dodo[index] = do
        suyeon[index] = su

    print(play(n, m, dodo, suyeon))


if __name__ == "__main__":
    main()
