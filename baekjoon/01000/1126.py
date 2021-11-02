import sys
from typing import List


IMP = -sys.maxsize
DIFF_RANGE = 500001

input = sys.stdin.readline


def stack_block(n: int, blocks: List[int]) -> int:
    cache = [[IMP for _ in range(DIFF_RANGE)] for _ in range(n)]
    cache[0][0] = 0
    cache[0][blocks[0]] = blocks[0]
    for bidx, block in enumerate(blocks[1:], 1):
        for diff in range(DIFF_RANGE):
            height: int = cache[bidx - 1][diff]
            if diff - block >= 0:
                height = max(height, block + cache[bidx - 1][diff - block])
            if block - diff >= 0:
                height = max(height, diff + cache[bidx - 1][block - diff])
            if diff + block < DIFF_RANGE:
                height = max(height, cache[bidx - 1][diff + block])
            cache[bidx][diff] = height
    return cache[n - 1][0]


def main() -> None:
    n = int(input())
    blocks = list(map(int, input().split()))

    height = stack_block(n, blocks)
    print(height if height > 0 else -1)


if __name__ == "__main__":
    main()
