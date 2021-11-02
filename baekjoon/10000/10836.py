import sys


input = sys.stdin.readline


def main() -> None:
    m, n = map(int, input().split())

    bound_length: int = 2 * m - 1
    grows = [0 for _ in range(bound_length)]
    for _ in range(n):
        zero, one, _ = map(int, input().split())
        if zero < bound_length:
            grows[zero] += 1
        if zero + one < bound_length:
            grows[zero + one] += 1

    grows[0] += 1
    for idx in range(1, bound_length):
        grows[idx] += grows[idx - 1]

    for ridx in range(m):
        row = [grows[m - ridx - 1]] + grows[m:]
        print(" ".join(map(str, row)))


if __name__ == "__main__":
    main()
