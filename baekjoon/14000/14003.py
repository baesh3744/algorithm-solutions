from bisect import bisect_left


def get_lis_infos(nums: list[int]) -> tuple[int, list[int]]:
    lis: list[int] = []
    indexes: list[int] = []

    for num in nums:
        if len(lis) == 0 or lis[-1] < num:
            lis.append(num)
            indexes.append(len(lis) - 1)
        else:
            idx: int = bisect_left(lis, num)
            lis[idx] = num
            indexes.append(idx)

    return len(lis), indexes


def get_lis(n: int, nums: list[int]) -> list[int]:
    lis_length, lis_indexes = get_lis_infos(nums)

    lis: list[int] = [-1 for _ in range(lis_length)]
    idx: int = lis_length - 1
    for pointer in range(n - 1, -1, -1):
        if lis_indexes[pointer] == idx:
            lis[idx] = nums[pointer]
            idx -= 1

    return lis


def main() -> None:
    n = int(input())
    nums = list(map(int, input().split()))

    lis: list[int] = get_lis(n, nums)
    print(len(lis))
    print(' '.join(map(str, lis)))


if __name__ == "__main__":
    main()
