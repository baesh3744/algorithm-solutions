import bisect
import sys


MAX: int = 100000

input = sys.stdin.readline


def accumulate(prime_list: list[int]) -> list[int]:
    has_to_add: bool = True
    acc_list: list[int] = [0 for _ in range(MAX + 1)]
    for start, end in zip(prime_list, prime_list[1:] + [MAX]):
        acc = acc_list[start - 1] + (3 if has_to_add else -1) * start
        has_to_add = not has_to_add
        for index in range(start, end + 1):
            acc_list[index] = acc
    return acc_list


def get_prime_list() -> list[int]:
    prime_list: list[int] = []
    is_prime_list: list[bool] = [True for _ in range(MAX + 1)]
    for prime in range(2, MAX + 1):
        if is_prime_list[prime]:
            prime_list.append(prime)
            for num in range(2 * prime, MAX + 1, prime):
                is_prime_list[num] = False
    return prime_list


def f(a: int, b: int) -> int:
    if bisect.bisect_left(prime_list, a) % 2 == 0:
        _list = acc_from_two_list
    else:
        _list = acc_from_three_list
    return _list[b] - _list[a - 1]


def main() -> None:
    global prime_list, acc_from_two_list, acc_from_three_list
    n = int(input())

    prime_list = get_prime_list()
    acc_from_two_list = accumulate(prime_list)
    acc_from_three_list = accumulate(prime_list[1:])

    for _ in range(n):
        a, b = map(int, input().split())
        print(f(a, b))


if __name__ == "__main__":
    main()
