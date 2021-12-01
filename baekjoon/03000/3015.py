import sys


input = sys.stdin.readline


def count(heights: list[int]) -> int:
    cnt: int = 0
    stack: list[list[int]] = []

    for height in heights:
        while stack and stack[-1][1] < height:
            cnt += stack[-1][0]
            stack.pop()

        cnt_height: int = 0

        if stack and stack[-1][1] == height:
            cnt_height, _ = stack.pop()
            cnt += cnt_height

        if stack:
            cnt += 1

        stack.append([cnt_height + 1, height])

    return cnt


if __name__ == "__main__":
    n = int(input())
    heights = [int(input()) for _ in range(n)]

    print(count(heights))
