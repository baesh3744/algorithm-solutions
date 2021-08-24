def main() -> None:
    p = [0, 1, 1, 1, 2, 2] + [-1] * 95
    for num in range(6, 101):
        p[num] = p[num - 1] + p[num - 5]

    t = int(input())
    for _ in range(t):
        n = int(input())
        print(p[n])


if __name__ == "__main__":
    main()
