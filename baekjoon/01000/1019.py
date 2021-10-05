def count(n: int) -> list[int]:
    counter: list[int] = [0 for _ in range(10)]
    divider: int = 1
    while divider <= n:
        left: int = n // (10 * divider)
        right: int = n % divider
        pivot: int = (n // divider) % 10
        for num in range(int(left == 0), 10):
            if num == 0:
                if pivot != 0:
                    counter[num] += left * divider
                else:
                    counter[num] += (left - 1) * divider + (right + 1)
            elif num < pivot:
                counter[num] += (left + 1) * divider
            elif num == pivot:
                counter[num] += left * divider + (right + 1)
            else:
                counter[num] += left * divider
        divider *= 10
    return counter


def main() -> None:
    n = int(input())
    print(" ".join(map(str, count(n))))


if __name__ == "__main__":
    main()
