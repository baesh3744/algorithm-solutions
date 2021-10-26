def get_length(n: int) -> int:
    length: int = 0
    while n:
        n //= 10
        length += 1
    return length


def write(n: int, k: int) -> int:
    length = get_length(n)
    cnt: int = 1
    number: int = n % k
    number_set: set[int] = set([])
    while number:
        if number in number_set:
            return -1
        number_set.add(number)
        number = ((10 ** length) * number + n) % k
        cnt += 1
    return cnt


def main() -> None:
    n, k = map(int, input().split())
    print(write(n, k))


if __name__ == "__main__":
    main()
