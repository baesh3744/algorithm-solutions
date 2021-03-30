from typing import Final, List
from itertools import permutations


MAX: Final[int] = 216000


def dp(hp1: int, hp2: int, hp3: int) -> int:
    if hp1 <= 0 and hp2 <= 0 and hp3 <= 0:
        return 0
    if cache[hp1][hp2][hp3] != -1:
        return cache[hp1][hp2][hp3]

    ret: int = MAX
    for attack1, attack2, attack3 in permutations([9, 3, 1], 3):
        hps: List[int] = [hp1 - attack1, hp2 - attack2, hp3 - attack3]

        hps = [0 if hp < 0 else hp for hp in hps]
        hps.sort()

        ret = min(ret, dp(hps[0], hps[1], hps[2]) + 1)

    cache[hp1][hp2][hp3] = ret
    return ret


def main() -> None:
    global cache
    _ = int(input())
    SCV = list(map(int, input().split()))

    cache = [[[-1 for _ in range(61)] for _ in range(61)] for _ in range(61)]

    while len(SCV) != 3:
        SCV.append(0)
    SCV.sort()
    print(dp(SCV[0], SCV[1], SCV[2]))


if __name__ == "__main__":
    main()
