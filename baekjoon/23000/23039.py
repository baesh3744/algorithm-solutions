import sys


input = sys.stdin.readline


def main() -> None:
    n = int(input())

    cross: list[int] = [0 for _ in range(6)]
    for _ in range(n):
        rabbit1, rabbit2 = map(int, input().split())
        if 2 <= abs(rabbit1 - rabbit2) <= 3:
            cross[rabbit1] += 1
            cross[rabbit2] += 1

    answer: int = 1
    cnt_cross: int = sum(cross) // 2
    if n == 10:
        answer = -1
    elif cnt_cross == 5:
        answer = 2
    elif cnt_cross < 2 or (cnt_cross == 2 and max(cross) == 2):
        answer = 0
    print(answer)


if __name__ == "__main__":
    main()
