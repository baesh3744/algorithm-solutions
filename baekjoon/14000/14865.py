import sys


input = sys.stdin.readline


def put_number_to_peak(n: int, lines: list[list[int]]) -> list[int]:
    start_with_neg: int = 2
    xs: list[int] = []

    for idx in range(n):
        curx, cury = lines[idx]
        _, nexty = lines[(idx + 1) % n]

        if cury * nexty < 0:
            xs.append(curx)
            if start_with_neg == 2:
                start_with_neg = int(nexty < 0)

    if start_with_neg == 1:
        xs.append(xs.pop(0))

    return [idx // 2 for idx, _ in sorted(enumerate(xs), key=lambda x: x[1])]


def count(n: int, lines: list[list[int]]) -> tuple[int, int]:
    cnt_inside: int = 0
    cnt_outside: int = 0
    stack: list[tuple[int, int]] = []

    numbers = put_number_to_peak(n, lines)
    for idx, num in enumerate(numbers):
        if stack and stack[-1][1] == num:
            if stack[-1][0] == idx - 1:
                cnt_inside += 1
            stack.pop()
        else:
            if not stack:
                cnt_outside += 1
            stack.append((idx, num))

    return cnt_outside, cnt_inside


if __name__ == "__main__":
    n = int(input())
    lines = [list(map(int, input().split())) for _ in range(n)]

    print(*count(n, lines))
