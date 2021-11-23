import sys


input = sys.stdin.readline

if __name__ == "__main__":
    _ = int(input())
    a = set(map(int, input().split()))
    _ = int(input())
    numbers = map(int, input().split())

    for num in numbers:
        print(int(num in a))
