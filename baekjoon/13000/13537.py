import sys
from bisect import bisect


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, n: int, a: list[int]) -> None:
        self.a = a
        self.tree: list[list[int]] = [[] for _ in range(4 * n)]

    def init(self, node: int, start: int, end: int) -> list[int]:
        if start == end:
            self.tree[node] = [self.a[start]]
            return self.tree[node]

        mid: int = (start + end) // 2
        left = self.init(2 * node, start, mid)
        right = self.init(2 * node + 1, mid + 1, end)
        self.tree[node] = self._merge(left, right)
        return self.tree[node]

    def search(
        self, node: int, start: int, end: int, left: int, right: int, k: int
    ) -> int:
        if end < left or right < start:
            return 0
        if left <= start and end <= right:
            return len(self.tree[node]) - bisect(self.tree[node], k)

        mid: int = (start + end) // 2
        return self.search(2 * node, start, mid, left, right, k) + (
            self.search(2 * node + 1, mid + 1, end, left, right, k)
        )

    def _merge(self, left: list[int], right: list[int]) -> list[int]:
        merged: list[int] = []
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


def main() -> None:
    n = int(input())
    a = list(map(int, input().split()))

    segment_tree = SegmentTree(n, a)
    segment_tree.init(1, 0, n - 1)

    m = int(input())
    for _ in range(m):
        i, j, k = map(int, input().split())
        print(segment_tree.search(1, 0, n - 1, i - 1, j - 1, k))


if __name__ == "__main__":
    main()
