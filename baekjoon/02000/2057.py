def main() -> None:
    n = int(input())

    if n == 0:
        print("NO")
        return

    num = 0
    cache = [1 for _ in range(21)]
    while cache[num] < n:
        cache[num + 1] = cache[num] * (num + 1)
        num += 1

    while n > 0 and num >= 0:
        if cache[num] <= n:
            n -= cache[num]
        num -= 1

    print("YES" if n == 0 else "NO")


if __name__ == "__main__":
    main()
