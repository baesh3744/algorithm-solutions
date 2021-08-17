import sys


input = sys.stdin.readline


def get_max_area(height_list: list[int]) -> int:
    if len(height_list) == 1:
        return height_list[0]

    max_area: int = 0
    start, end = 0, len(height_list) - 1
    mid: int = (start + end) // 2
    left_ptr, right_ptr = mid, mid + 1

    while True:
        height: int = min(height_list[left_ptr], height_list[right_ptr])
        while start <= left_ptr - 1 and height <= height_list[left_ptr - 1]:
            left_ptr -= 1
        while right_ptr + 1 <= end and height <= height_list[right_ptr + 1]:
            right_ptr += 1

        max_area = max(max_area, (right_ptr - left_ptr + 1) * height)

        if left_ptr == start and right_ptr == end:
            break

        if left_ptr == start or (
            right_ptr != end and height_list[left_ptr - 1] < height_list[right_ptr + 1]
        ):
            right_ptr += 1
        else:
            left_ptr -= 1

    return max(
        max_area,
        get_max_area(height_list[: mid + 1]),
        get_max_area(height_list[mid + 1 :]),
    )


def main() -> None:
    while True:
        number_list = list(map(int, input().split()))
        if number_list[0] == 0:
            break
        print(get_max_area(number_list[1:]))


if __name__ == "__main__":
    main()
