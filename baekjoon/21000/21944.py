import sys
from collections import defaultdict
from heapq import heappop, heappush


NOT_FOUND = -1000000

Info = tuple[int, int, int]

input = sys.stdin.readline


def add(pb: int, lv: int, algo: int) -> None:
    heappush(asc_algo[algo], (lv, pb, algo))
    heappush(dsc_algo[algo], (-lv, -pb, -algo))
    heappush(asc_lv[lv], (lv, pb, algo))
    heappush(dsc_lv[lv], (-lv, -pb, -algo))
    pb_infos[pb] = (lv, algo)
    removed.difference_update([(lv, pb, algo), (-lv, -pb, -algo)])


def recommend(infos: list[Info]) -> int:
    while infos and infos[0] in removed:
        heappop(infos)
    if infos:
        _, pb, _ = infos[0]
        return abs(pb)
    return NOT_FOUND


def recommend_easy(min_level: int = -200) -> int:
    levels = sorted(asc_lv.keys())
    for level in levels:
        if level < min_level:
            continue
        pb = recommend(asc_lv[level])
        if pb != NOT_FOUND:
            return pb
    return -1


def recommend_difficult(max_level: int = 200) -> int:
    levels = sorted(dsc_lv.keys(), reverse=True)
    for level in levels:
        if level >= max_level:
            continue
        pb = recommend(dsc_lv[level])
        if pb != NOT_FOUND:
            return pb
    return -1


if __name__ == "__main__":
    asc_algo: defaultdict[int, list[Info]] = defaultdict(list)
    dsc_algo: defaultdict[int, list[Info]] = defaultdict(list)
    asc_lv: defaultdict[int, list[Info]] = defaultdict(list)
    dsc_lv: defaultdict[int, list[Info]] = defaultdict(list)
    pb_infos: dict[int, tuple[int, int]] = dict()
    removed: set[Info] = set()

    n = int(input())
    for _ in range(n):
        p, l, g = map(int, input().split())
        add(p, l, g)

    m = int(input())
    for _ in range(m):
        cmd, *args = input().split()

        if cmd == "recommend":
            g, x = map(int, args)
            if x == 1:
                print(recommend(dsc_algo[g]))
            else:  # -1
                print(recommend(asc_algo[g]))

        elif cmd == "recommend2":
            x = int(args[0])
            if x == 1:
                print(recommend_difficult())
            else:  # -1
                print(recommend_easy())

        elif cmd == "recommend3":
            x, l = map(int, args)
            if x == 1:
                print(recommend_easy(min_level=l))
            else:  # -1
                print(recommend_difficult(max_level=l))

        elif cmd == "add":
            p, l, g = map(int, args)
            add(p, l, g)

        else:  # "solved"
            p = int(args[0])
            lv, algo = pb_infos[p]
            removed.update([(lv, p, algo), (-lv, -p, -algo)])
