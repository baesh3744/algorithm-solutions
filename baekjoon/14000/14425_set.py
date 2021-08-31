import sys


input = sys.stdin.readline


def main() -> None:
    n, m = map(int, input().split())
    string_set = set([input() for _ in range(n)])

    cnt: int = 0
    for _ in range(m):
        if input() in string_set:
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
