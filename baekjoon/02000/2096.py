import sys


MAX = sys.maxsize
input = sys.stdin.readline

if __name__ == "__main__":
    n = int(input())

    max_cache: list[list[int]] = [[0 for _ in range(3)] for _ in range(2)]
    min_cache: list[list[int]] = [[0 for _ in range(3)] for _ in range(2)]

    for idx in range(1, n + 1):
        row = list(map(int, input().split()))

        cache_idx: int = idx % 2
        prev_idx: int = 1 - cache_idx

        max_cache[cache_idx][0] = max(max_cache[prev_idx][0:2]) + row[0]
        max_cache[cache_idx][1] = max(max_cache[prev_idx][0:3]) + row[1]
        max_cache[cache_idx][2] = max(max_cache[prev_idx][1:3]) + row[2]

        min_cache[cache_idx][0] = min(min_cache[prev_idx][0:2]) + row[0]
        min_cache[cache_idx][1] = min(min_cache[prev_idx][0:3]) + row[1]
        min_cache[cache_idx][2] = min(min_cache[prev_idx][1:3]) + row[2]

    print(max(max_cache[n % 2]), min(min_cache[n % 2]))
