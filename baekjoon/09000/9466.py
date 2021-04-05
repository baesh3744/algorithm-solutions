from typing import List, Tuple


def make_team(snum: int, tnum: int, selected: List[int], checked: List[int]) -> Tuple[int, List[int]]:
    no_team: int = 0
    while checked[snum] == 0:
        checked[snum] = tnum
        no_team += 1
        snum = selected[snum]

    while checked[snum] == tnum:
        checked[snum] = -1
        no_team -= 1
        snum = selected[snum]

    return no_team, checked


def count_no_team(n: int, selected: List[int]) -> int:
    # 0: 방문 x
    # -1: 방문 o and 팀 o
    # tnum: 방문 o and 팀 x
    checked: List[int] = [0 for _ in range(n + 1)]
    ans: int = 0
    tnum: int = 1

    for snum in range(1, n + 1):
        if checked[snum] == 0:
            no_team, checked = make_team(snum, tnum, selected, checked)
            ans += no_team
            tnum += 1

    return ans


def main() -> None:
    T = int(input())

    for _ in range(T):
        n = int(input())
        selected = list(map(int, input().split()))
        selected.insert(0, 0)
        print(count_no_team(n, selected))


if __name__ == "__main__":
    main()
