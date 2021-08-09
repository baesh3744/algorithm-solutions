def main() -> None:
    cache = [True for _ in range(10001)]
    for num in range(10001):
        while True:
            num += sum(map(int, (str(num))))
            if num > 10000 or not cache[num]:
                break
            cache[num] = False
    print(" ".join([str(index) for index, value in enumerate(cache) if value]))


if __name__ == "__main__":
    main()
