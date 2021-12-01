import sys
from bisect import bisect_left
from typing import List


input = sys.stdin.readline


class MergeSortTree:
    def __init__(self, n: int, powers: List[int]) -> None:
        self.powers = powers
        self.tree: List[List[int]] = [[] for _ in range(4 * n)]
        self.init(1, 0, n - 1)

    def init(self, node: int, start: int, end: int) -> List[int]:
        if start == end:
            self.tree[node] = [self.powers[start]]
            return self.tree[node]

        mid: int = (start + end) // 2
        left: List[int] = self.init(2 * node, start, mid)
        right: List[int] = self.init(2 * node + 1, mid + 1, end)
        self.tree[node] = self.merge(left, right)
        return self.tree[node]

    def merge(self, left: List[int], right: List[int]) -> List[int]:
        merged: List[int] = []
        lidx, ridx, llength, rlength = 0, 0, len(left), len(right)

        while lidx < llength and ridx < rlength:
            if left[lidx] <= right[ridx]:
                merged.append(left[lidx])
                lidx += 1
            else:
                merged.append(right[ridx])
                ridx += 1

        while lidx < llength:
            merged.append(left[lidx])
            lidx += 1

        while ridx < rlength:
            merged.append(right[ridx])
            ridx += 1

        return merged

    def query(self, node: int, start: int, end: int, idx: int) -> int:
        if idx < start:
            return 0
        if end <= idx:
            return end - start + 1 - bisect_left(self.tree[node], self.powers[idx])

        mid: int = (start + end) // 2
        left: int = self.query(2 * node, start, mid, idx)
        right: int = self.query(2 * node + 1, mid + 1, end, idx)
        return left + right


if __name__ == "__main__":
    n = int(input())
    powers = [int(input()) for _ in range(n)]

    mstree = MergeSortTree(n, powers)
    for idx in range(n):
        print(mstree.query(1, 0, n - 1, idx))
