def count_number_of_digits(N: int) -> int:
    ret: int = 0
    while(N >= 1):
        N /= 10
        ret += 1
    return ret


def main() -> None:
    N: int = int(input())

    ans: int = 0
    base: int = 1
    nod: int = count_number_of_digits(N)
    for i in range(1, nod):
        ans += i * (9 * base)  # 10 * base - base
        base *= 10
    ans += nod * (N // base - 1) * base
    ans += nod * (N % base + 1)
    print(ans)


if __name__ == "__main__":
    main()
