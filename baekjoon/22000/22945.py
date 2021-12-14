import sys


input = sys.stdin.readline


def build_team() -> int:
    ans: int = 0
    lidx: int = 0
    ridx: int = n - 1

    while lidx < ridx:
        left: int = xs[lidx]
        right: int = xs[ridx]

        ans = max(ans, (ridx - lidx - 1) * min(left, right))

        if left < right:
            lidx += 1
        else:
            ridx -= 1

    return ans


if __name__ == "__main__":
    n = int(input())
    xs = list(map(int, input().split()))

    print(build_team())
