import sys
from heapq import heappop, heappush
from math import ceil


input = sys.stdin.readline


def list_medians(nums: list[int]) -> list[int]:
    medians: list[int] = []
    bigger: list[int] = []
    smaller: list[int] = []
    heap: list[int] = []

    # 1번째 수
    medians.append(nums[0])

    # 3번쨰 수
    if len(nums) >= 3:
        for idx in range(3):
            heappush(heap, nums[idx])
        heappush(smaller, -heappop(heap))
        medians.append(heappop(heap))
        heappush(bigger, heappop(heap))

    for idx in range(4, len(nums), 2):
        heappush(heap, nums[idx - 1])
        heappush(heap, nums[idx])
        heappush(heap, medians[-1])
        heappush(heap, -heappop(smaller))
        heappush(heap, heappop(bigger))

        for _ in range(2):
            heappush(smaller, -heappop(heap))
        medians.append(heappop(heap))
        for _ in range(2):
            heappush(bigger, heappop(heap))

    return medians


def print_answer(medians: list[int]) -> None:
    length: int = len(medians)
    print(length)
    for line in range(0, length, 10):
        print(" ".join(map(str, medians[line : line + 10])))


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        m = int(input())

        nums: list[int] = []
        for _ in range(ceil(m / 10)):
            nums.extend(list(map(int, input().split())))

        medians = list_medians(nums)
        print_answer(medians)
