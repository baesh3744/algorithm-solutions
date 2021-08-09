import heapq
import sys
from collections import defaultdict


input = sys.stdin.readline


def count_room(lecture_list: defaultdict[int, list[int]], start_list: list[int]) -> int:
    cnt_room: int = 0
    end_list: list[int] = []
    for start in start_list:
        while end_list and end_list[0] <= start:
            heapq.heappop(end_list)
        for end in lecture_list[start]:
            heapq.heappush(end_list, end)
        cnt_room = max(cnt_room, len(end_list))
    return cnt_room


def main() -> None:
    n = int(input())

    lecture_list: defaultdict[int, list[int]] = defaultdict(list)
    start_list: set[int] = set()
    for _ in range(n):
        s, t = map(int, input().split())
        lecture_list[s].append(t)
        start_list.add(s)

    print(count_room(lecture_list, sorted(start_list)))


if __name__ == "__main__":
    main()
