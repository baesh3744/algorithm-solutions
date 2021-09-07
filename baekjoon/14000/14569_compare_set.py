import sys


input = sys.stdin.readline


def main() -> None:
    n = int(input())

    hour_list: list[set[int]] = [set(map(int, input().split()[1:])) for _ in range(n)]

    m = int(input())
    for _ in range(m):
        std_list = set(map(int, input().split()[1:]))
        print(sum(1 for hour in hour_list if std_list.issuperset(hour)))


if __name__ == "__main__":
    main()

# reference "thenitromefan"
# https://www.acmicpc.net/source/24088248
