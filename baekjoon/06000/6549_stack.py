import sys


input = sys.stdin.readline


def get_max_area(height_list: list[int]) -> int:
    max_area: int = 0
    stack: list[int] = [-1]
    height_list.append(0)
    for index, height in enumerate(height_list):
        while stack and height_list[stack[-1]] > height:
            sub_height: int = height_list[stack.pop()]
            sub_width: int = index - stack[-1] - 1
            max_area = max(max_area, sub_height * sub_width)
        stack.append(index)
    return max_area


def main() -> None:
    while True:
        number_list = list(map(int, input().split()))
        if number_list[0] == 0:
            break
        print(get_max_area(number_list[1:]))


if __name__ == "__main__":
    main()
