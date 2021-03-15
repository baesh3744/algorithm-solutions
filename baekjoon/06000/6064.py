from math import gcd


def solve(M: int, N: int, x: int, y: int) -> None:
    lcm: int = int(M * N / gcd(M, N))
    ans: int = x
    if y == N:
        y = 0
    while ans <= lcm:
        if ans % N == y:
            print(ans)
            return
        ans += M
    print(-1)
    return


def main() -> None:
    T = int(input())
    for t in range(T):
        M, N, x, y = map(int, input().split())
        solve(M, N, x, y)


if __name__ == "__main__":
    main()
