import sys
from bisect import bisect_left


input = sys.stdin.readline


def get_lis_length(array: list[int]) -> int:
    lis: list[int] = []

    for number in array:
        if len(lis) == 0 or lis[-1] < number:
            lis.append(number)
        else:
            lis[bisect_left(lis, number)] = number

    return len(lis)


def main() -> None:
    _ = int(input())
    array = list(map(int, input().split()))

    print(get_lis_length(array))


if __name__ == "__main__":
    main()
