from typing import List


def get_pair_count(x: int, seq: List[int]) -> int:
    count: int = 0
    start: int = 0
    end: int = len(seq) - 1

    while start < end:
        sub_sum: int = seq[start] + seq[end]
        if sub_sum == x:
            count += 1
        if sub_sum <= x:
            start += 1
        if sub_sum >= x:
            end -= 1

    return count


def main() -> None:
    _ = int(input())
    seq = list(map(int, input().split()))
    x = int(input())

    print(get_pair_count(x, sorted(seq)))


if __name__ == "__main__":
    main()
