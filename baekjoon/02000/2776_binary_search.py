import bisect
import sys


input = sys.stdin.readline


def main() -> None:
    t = int(input())
    for _ in range(t):
        n = int(input())
        note1 = sorted(map(int, input().split()))
        _ = int(input())
        note2 = list(map(int, input().split()))

        for num in note2:
            index = bisect.bisect_left(note1, num, hi=n - 1)
            print(1 if note1[index] == num else 0)


if __name__ == "__main__":
    main()
