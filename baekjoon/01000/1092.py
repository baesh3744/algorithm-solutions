from itertools import accumulate
from math import ceil
import sys


input = sys.stdin.readline


def count_time(weights: list[int], limits: list[int]) -> int:
    index: int = 0
    time: int = 0
    boxes: list[int] = [0] * len(limits)

    for weight in weights:
        while weight > limits[index]:
            index += 1
        boxes[index] += 1

    accumulated_boxes = accumulate(reversed(boxes))
    for index, acc in enumerate(accumulated_boxes):
        time = max(time, ceil(acc / (index + 1)))

    return time


def main() -> None:
    _ = int(input())
    limits = sorted(map(int, input().split()))
    _ = int(input())
    weights = sorted(map(int, input().split()))

    if weights[-1] > limits[-1]:
        print("-1")
    else:
        print(count_time(weights, limits))


if __name__ == "__main__":
    main()
