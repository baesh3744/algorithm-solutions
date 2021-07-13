import sys


Board = list[list[str]]


def get_max_student(ridx: int, prev: int) -> int:
    if ridx >= n:
        return 0
    if cache[ridx][prev] != -1:
        return cache[ridx][prev]

    max_student: int = 0
    for cur in range(2 ** m):
        cur_student: int = 0
        is_possible: bool = True

        for cidx in range(m):
            if cur & (1 << cidx):
                cur_student += 1
                if board[ridx][m - 1 - cidx] == 'x' or \
                        (cidx - 1 >= 0 and cur & (1 << cidx - 1)) or \
                        (cidx - 1 >= 0 and prev & (1 << cidx - 1)) or \
                        (cidx + 1 < m and cur & (1 << cidx + 1)) or \
                        (cidx + 1 < m and prev & (1 << cidx + 1)):
                    is_possible = False
                    break

        if is_possible:
            max_student = max(max_student,
                              get_max_student(ridx + 1, cur) + cur_student)

    cache[ridx][prev] = max_student
    return cache[ridx][prev]


def main() -> None:
    global n, m, board, cache
    c = int(input())
    for _ in range(c):
        n, m = map(int, sys.stdin.readline().split())
        board = [list(sys.stdin.readline().strip()) for _ in range(n)]
        cache = [[-1 for _ in range(2 ** m)] for _ in range(n)]
        print(get_max_student(0, 0))


if __name__ == "__main__":
    main()
