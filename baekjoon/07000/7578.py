import sys
from typing import Dict


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, n: int) -> None:
        self.tree = [0 for _ in range(4 * n)]

    def update(self, node: int, start: int, end: int, idx: int) -> None:
        if idx < start or end < idx:
            return

        self.tree[node] += 1

        if start != end:
            mid: int = (start + end) // 2
            self.update(2 * node, start, mid, idx)
            self.update(2 * node + 1, mid + 1, end, idx)

    def count(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid: int = (start + end) // 2
        return self.count(2 * node, start, mid, left, right) + self.count(
            2 * node + 1, mid + 1, end, left, right
        )


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))

    id2index: Dict[int, int] = {}
    for idx, bid in enumerate(b):
        id2index[bid] = idx

    cnt: int = 0
    tree: SegmentTree = SegmentTree(n)
    for aid in a:
        idx: int = id2index[aid]
        cnt += tree.count(1, 0, n - 1, idx + 1, n - 1)
        tree.update(1, 0, n - 1, idx)
    print(cnt)
