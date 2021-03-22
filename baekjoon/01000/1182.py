from typing import List
import itertools


def solve(numbers: List[int], S: int) -> None:
    ans: int = 0
    for ncr_length in range(1, len(numbers) + 1):
        for ncr in itertools.combinations(range(len(numbers)), ncr_length):
            sub_sum: int = 0
            for item in ncr:
                sub_sum += numbers[item]

            if sub_sum == S:
                ans += 1
    print(ans)


def main() -> None:
    _, S = map(int, input().split())
    numbers = list(map(int, input().split()))
    solve(numbers, S)


if __name__ == "__main__":
    main()
