def main() -> None:
    _ = int(input())
    a = sorted(map(int, input().split()))
    b = sorted(map(int, input().split()), reverse=True)

    print(sum(map(lambda x: x[0] * x[1], zip(a, b))))


if __name__ == "__main__":
    main()
