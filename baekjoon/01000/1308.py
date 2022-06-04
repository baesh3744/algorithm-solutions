import sys
from datetime import date


input = sys.stdin.readline


def main() -> None:
    today = date(*map(int, input().split()))
    target = date(*map(int, input().split()))

    after_1000_years = today.replace(year=today.year + 1000)
    if after_1000_years <= target:
        print("gg")
    else:
        print(f"D-{(target - today).days}")


if __name__ == "__main__":
    main()
