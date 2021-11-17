import sys


input = sys.stdin.readline


def get_max_area(start: int, end: int) -> int:
    if start == end:
        return height_list[start]

    mid: int = (start + end) // 2
    left: int = mid
    right: int = mid + 1
    height: int = min(height_list[left], height_list[right])
    max_area: int = 2 * height

    while start < left or right < end:
        if right == end or (
            start < left and height_list[right + 1] <= height_list[left - 1]
        ):
            left -= 1
            height = min(height, height_list[left])
        else:
            right += 1
            height = min(height, height_list[right])
        max_area = max(max_area, height * (right - left + 1))

    return max(max_area, get_max_area(start, mid), get_max_area(mid + 1, end))


if __name__ == "__main__":
    n = int(input())
    height_list = [int(input()) for _ in range(n)]

    print(get_max_area(0, n - 1))
