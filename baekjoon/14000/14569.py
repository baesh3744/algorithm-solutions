import sys


input = sys.stdin.readline


def count(n: int, hour_list: list[set[int]], std_list: list[int]) -> list[int]:
    std_count_list: list[int] = [0 for _ in range(n)]
    for std_hour in std_list[1:]:
        for index, hour_set in enumerate(hour_list):
            if std_hour in hour_set:
                std_count_list[index] += 1
    return std_count_list


def main() -> None:
    n = int(input())

    count_list: list[int] = [-1 for _ in range(n)]
    hour_list: list[set[int]] = [set() for _ in range(n)]
    for index in range(n):
        kt = list(map(int, input().split()))
        count_list[index] = kt[0]
        hour_list[index] = set(kt[1:])

    m = int(input())
    for _ in range(m):
        std_list = list(map(int, input().split()))
        std_count_list = count(n, hour_list, std_list)
        print(
            sum(
                std_count == count
                for std_count, count in zip(std_count_list, count_list)
            )
        )


if __name__ == "__main__":
    main()
