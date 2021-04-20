def main() -> None:
    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())
        print(min((N + M) // 12, N // 5))


if __name__ == "__main__":
    main()
