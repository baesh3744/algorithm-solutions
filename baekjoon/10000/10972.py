def reorder(number_list: list[int]) -> list[int]:
    first: int = number_list[0]
    bigger: list[int] = sorted(filter(lambda x: x > first, number_list))
    smaller: list[int] = sorted(filter(lambda x: x <= first, number_list))
    return [bigger[0]] + smaller + bigger[1:]


def get_next(n: int, number_list: list[int]) -> list[int]:
    for index in range(n - 2, -1, -1):
        if number_list[index] < number_list[index + 1]:
            return number_list[:index] + reorder(number_list[index:])
    return [-1]


def main() -> None:
    n = int(input())
    number_list = list(map(int, input().split()))

    print(" ".join(map(str, get_next(n, number_list))))


if __name__ == "__main__":
    main()
