import sys
from heapq import heappop, heappush


input = sys.stdin.readline


def get_max_ramen(problem_list: list[list[int]]) -> int:
    cnt_ramen: int = 0
    ramens: list[int] = []

    for deadline, ramen in sorted(problem_list):
        heappush(ramens, ramen)
        cnt_ramen += 1

        if cnt_ramen > deadline:
            heappop(ramens)
            cnt_ramen -= 1

    return sum(ramens)


if __name__ == "__main__":
    n = int(input())
    problem_list = [list(map(int, input().split())) for _ in range(n)]

    print(get_max_ramen(problem_list))
