def main() -> None:
    N = int(input())
    sn = [input() for _ in range(N)]

    Q = int(input())
    for _ in range(Q):
        sq = input()

        ans: int = 0
        for s in sn:
            if s.find(sq) != -1:
                ans += 1
        print(ans)


if __name__ == "__main__":
    main()
