import sys


MOD = 1000003

Matrix = list[list[int]]

input = sys.stdin.readline


def multiply_matrix(a: Matrix, b: Matrix) -> Matrix:
    length = len(a)
    multiplied = [[0 for _ in range(length)] for _ in range(length)]
    for ridx in range(length):
        for cidx in range(length):
            for through in range(length):
                multiplied[ridx][cidx] += a[ridx][through] * b[through][cidx]
            multiplied[ridx][cidx] %= MOD
    return multiplied


def convert(n: int, inputA: Matrix) -> Matrix:
    a = [[0 for _ in range(5 * n)] for _ in range(5 * n)]
    for node in range(n):
        for dist in range(1, 5):
            a[5 * node + dist][5 * node + dist - 1] = 1
    for start, row in enumerate(inputA):
        for end, elmt in enumerate(row):
            if elmt > 0:
                a[5 * start][5 * end + elmt - 1] = 1
    return a


def pow_matrix(a: Matrix, t: int) -> Matrix:
    if t == 1:
        return a
    ret = pow_matrix(a, t // 2)
    ret = multiply_matrix(ret, ret)
    if t & 1 == 1:
        ret = multiply_matrix(ret, a)
    return ret


def main() -> None:
    n, s, e, t = map(int, input().split())

    inputA = [list(map(int, list(input().strip()))) for _ in range(n)]

    a = convert(n, inputA)
    answer = pow_matrix(a, t)
    print(answer[5 * (s - 1)][5 * (e - 1)])


if __name__ == "__main__":
    main()
