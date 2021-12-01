import sys


input = sys.stdin.readline


def count_cutting(max_length: int) -> tuple[int, int]:
    cnt: int = 0
    sublength: int = 0

    for length in lengths:
        if length > max_length:
            return -1, -1

        sublength += length
        if sublength > max_length:
            sublength = length
            cnt += 1

    return cnt + 1, sublength


def solve() -> tuple[int, int]:
    first_cutting: int = 0
    start: int = 0
    end: int = l

    while start <= end:
        mid: int = (start + end) // 2

        cnt, first = count_cutting(mid)
        if 0 <= cnt <= c + 1:
            end = mid - 1
            first_cutting = first if cnt == c + 1 else cuttings[1]
        else:
            start = mid + 1

    return start, first_cutting


if __name__ == "__main__":
    l, k, c = map(int, input().split())
    cuttings = [0] + list(set(map(int, input().split()))) + [l]

    cuttings.sort()
    lengths = [
        cuttings[idx] - cuttings[idx - 1] for idx in range(len(cuttings) - 1, 0, -1)
    ]
    print(*solve())
