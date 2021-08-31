import math


def get_prime_list(m: int, n: int) -> list[int]:
    prime_list: list[bool] = [True for _ in range(n + 1)]
    for prime in range(2, math.floor(math.sqrt(n)) + 1):
        if prime_list[prime]:
            num: int = 2 * prime
            while num <= n:
                prime_list[num] = False
                num += prime
    start: int = max(2, m)
    return [
        index + start for index, is_prime in enumerate(prime_list[start:]) if is_prime
    ]


def main() -> None:
    m, n = map(int, input().split())

    prime_list = get_prime_list(m, n)
    for prime in prime_list:
        print(prime)


if __name__ == "__main__":
    main()
