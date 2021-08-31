import sys


input = sys.stdin.readline


def main() -> None:
    t = int(input())
    for _ in range(t):
        _ = int(input())
        note = set(input().split())
        _ = int(input())
        print("\n".join("1" if num in note else "0" for num in input().split()))


if __name__ == "__main__":
    main()

# reference "kkhe56"
