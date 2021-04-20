from typing import List


def get_min_impossible(arr: List[int]) -> int:
    if arr[0] != 1:
        return 1

    sum: int = 0
    for num in arr:
        if sum != 0 and sum + 1 < num:
            break
        sum += num
    return sum + 1


def main() -> None:
    _ = int(input())
    nums = list(map(int, input().split()))

    print(get_min_impossible(sorted(nums)))


if __name__ == "__main__":
    main()
