import sys


input = sys.stdin.readline


def get_remainder(number: int, count: int, divisor: int) -> int:
    if count == 1:
        return number % divisor

    sub_remainder = get_remainder(number, count // 2, divisor)
    divided_number = sub_remainder * sub_remainder

    if count % 2 == 1:
        divided_number *= number

    return divided_number % divisor


def main() -> None:
    a, b, c = map(int, input().split())

    print(get_remainder(a, b, c))


if __name__ == "__main__":
    main()
