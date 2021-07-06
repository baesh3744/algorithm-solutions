import sys


def count_paper(wrong: list[int], size: int):
    cnt: int = 0
    end: int = -1
    for row in wrong:
        if row > end:
            end = row + size - 1
            cnt += 1
    return cnt


def get_paper_size(start: int, end: int, paper: int, wrong: list[int]):
    while start <= end:
        mid: int = (start + end) // 2

        cnt = count_paper(wrong, mid)
        if cnt <= paper:
            end = mid - 1
        else:
            start = mid + 1

    return start


def main() -> None:
    row, _ = map(int, input().split())
    paper = int(input())
    cnt_wrong = int(input())

    min_size: int = -1
    wrong: list[int] = []
    for _ in range(cnt_wrong):
        r, c = map(int, sys.stdin.readline().split())
        wrong.append(c)
        min_size = max(min_size, r)

    wrong = sorted(list(set(wrong)))
    print(get_paper_size(min_size, row, paper, wrong))


if __name__ == "__main__":
    main()
