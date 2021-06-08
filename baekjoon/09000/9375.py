import sys


def main() -> None:
    test_case = int(input())

    for _ in range(test_case):
        clothes: dict[str, int] = dict()

        n = int(sys.stdin.readline())
        for _ in range(n):
            _, category = map(str, sys.stdin.readline().split())
            if category in clothes:
                clothes[category] += 1
            else:
                clothes[category] = 2

        num_case: int = 1
        for value in clothes.values():
            num_case *= value
        print(num_case - 1)


if __name__ == "__main__":
    main()
