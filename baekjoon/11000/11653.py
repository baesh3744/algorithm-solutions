def main() -> None:
    n = int(input())

    num: int = 2
    while n % num == 0:
        print(num)
        n /= num

    num = 3
    while num <= n:
        if n % num == 0:
            print(num)
            n /= num
        else:
            num += 2


if __name__ == "__main__":
    main()
