import sys


MOVE_LIST = [(0, 1), (1, 0)]

input = sys.stdin.readline


def cut(used: int) -> int:
    if used == all_used:
        return 0
    if cache[used] != -1:
        return cache[used]

    max_sum: int = -1
    for cur in range(n * m):
        if used & (1 << cur) > 0:
            continue

        ridx, cidx = cur // m, cur % m
        for move_ridx, move_cidx in MOVE_LIST:
            next_used: int = used
            num: int = 0

            for length in range(4):
                next_ridx: int = ridx + length * move_ridx
                next_cidx: int = cidx + length * move_cidx
                next_: int = 1 << (next_ridx * m + next_cidx)
                if next_ridx >= n or next_cidx >= m or (next_used & next_) > 0:
                    break

                next_used += next_
                num = 10 * num + board[next_ridx][next_cidx]
                max_sum = max(max_sum, num + cut(next_used))
        break

    cache[used] = max_sum
    return max_sum


if __name__ == "__main__":
    n, m = map(int, input().split())
    board = [list(map(int, list(input().strip()))) for _ in range(n)]

    all_used: int = (1 << n * m) - 1
    cache: list[int] = [-1 for _ in range(all_used)]
    print(cut(0))
