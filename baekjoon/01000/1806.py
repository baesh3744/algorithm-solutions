from typing import Final


MAX_LEN: Final[int] = 100000


def solve(n: int, s: int, nums: list[int]) -> int:
    min_len: int = MAX_LEN
    start_idx: int = 0
    end_idx: int = 0
    sub_sum: int = 0

    while end_idx < n:
        sub_sum += nums[end_idx]

        while start_idx <= end_idx and sub_sum - nums[start_idx] >= s:
            sub_sum -= nums[start_idx]
            start_idx += 1

        if sub_sum >= s:
            min_len = min(min_len, end_idx - start_idx + 1)

        end_idx += 1

    return 0 if min_len == MAX_LEN else min_len


def main() -> None:
    n, s = map(int, input().split())
    nums = list(map(int, input().split()))

    print(solve(n, s, nums))


if __name__ == "__main__":
    main()
