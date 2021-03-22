from typing import List
import itertools


def get_sub_sums(N: int, S: List[int]) -> List[int]:
    sub_sums: List[int] = []
    for length in range(1, N + 1):
        for sets in itertools.combinations(S, length):
            sub_sum: int = 0
            for item in sets:
                sub_sum += item
            sub_sums.append(sub_sum)
    sub_sums = list(dict.fromkeys(sub_sums))
    sub_sums.sort()
    return sub_sums


def find(list: List[int]) -> int:
    ret: int = 1
    for number in range(1, 2200000):
        if number > len(list) or number != list[number - 1]:
            ret = number
            break
    return ret


def solve(N: int, S: List[int]) -> None:
    sub_sums: List[int] = get_sub_sums(N, S)
    print(find(sub_sums))


def main() -> None:
    N = int(input())
    S = list(map(int, input().split()))
    solve(N, S)


if __name__ == "__main__":
    main()
