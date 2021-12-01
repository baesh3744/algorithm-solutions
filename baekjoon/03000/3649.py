import sys


input = sys.stdin.readline


def can_block(n: int, x: int, legos: list[int]) -> tuple[bool, int, int]:
    sidx: int = 0
    eidx: int = n - 1

    while sidx < eidx:
        width: int = legos[sidx] + legos[eidx]

        if width == x:
            return True, legos[sidx], legos[eidx]
        elif width < x:
            sidx += 1
        else:
            eidx -= 1

    return False, -1, -1


if __name__ == "__main__":
    while True:
        try:
            x = int(input()) * 10_000_000
            n = int(input())
            legos = [int(input()) for _ in range(n)]

            blocked, l1, l2 = can_block(n, x, sorted(legos))
            if blocked:
                print(f"yes {l1} {l2}")
            else:
                print("danger")

        except:
            break
