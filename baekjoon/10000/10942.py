import sys
from typing import List


cache: List[List[int]] = []
nums: List[int] = []


def is_palindrome(s: int, e: int) -> int:
    global cache
    if e <= s:
        return 1
    if cache[s][e] != -1:
        return cache[s][e]

    if nums[s] == nums[e] and is_palindrome(s + 1, e - 1) == 1:
        cache[s][e] = 1
    else:
        cache[s][e] = 0
    return cache[s][e]


def main() -> None:
    global nums, cache
    n = int(input())
    nums = list(map(int, input().split()))
    m = int(input())
    cache = [[-1 for _ in range(n)] for _ in range(n)]

    for _ in range(m):
        s, e = map(int, sys.stdin.readline().split())
        print(is_palindrome(s - 1, e - 1))


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
