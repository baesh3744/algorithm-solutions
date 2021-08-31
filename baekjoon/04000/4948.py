import sys


input = sys.stdin.readline


def count(n: int) -> int:
    cnt: int = 0
    prime_list: list[bool] = [True for _ in range(2 * n + 1)]
    for prime in range(2, 2 * n + 1):
        if prime_list[prime]:
            cnt += 1 if prime > n else 0
            num: int = 2 * prime
            while num <= 2 * n:
                prime_list[num] = False
                num += prime
    return cnt


def main() -> None:
    while True:
        n = int(input())
        if n == 0:
            break
        print(count(n))


if __name__ == "__main__":
    main()
