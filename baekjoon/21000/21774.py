import bisect
import sys


input = sys.stdin.readline


def main() -> None:
    n, q = map(int, input().split())

    log_list: list[list[str]] = [[] for _ in range(7)]
    for _ in range(n):
        log = [char for char in input() if char.isdigit()]
        log_list[int(log[-1])].append("".join(log[:-1]))

    for _ in range(q):
        query = [char for char in input() if char.isdigit()]
        start_query = "".join(query[:14])
        end_query = "".join(query[14:28])

        cnt: int = 0
        for level in range(int(query[28]), 7):
            start = bisect.bisect_left(log_list[level], start_query)
            end = bisect.bisect_right(log_list[level], end_query)
            cnt += end - start
        print(cnt)


if __name__ == "__main__":
    main()
