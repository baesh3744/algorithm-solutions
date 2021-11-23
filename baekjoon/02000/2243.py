import sys


IMP = sys.maxsize
FLAVOR = 1000000

input = sys.stdin.readline


class SegmentTree:
    def __init__(self) -> None:
        self.tree = [0 for _ in range(4 * FLAVOR)]

    def get(self, node: int, start: int, end: int, priority: int) -> int:
        if priority > self.tree[node]:
            return IMP

        self.tree[node] -= 1

        if start == end:
            return start

        mid: int = (start + end) // 2
        if (left := self.get(2 * node, start, mid, priority)) != IMP:
            return left
        return self.get(2 * node + 1, mid + 1, end, priority - self.tree[2 * node])

    def update(self, node: int, start: int, end: int, value: int, cnt: int) -> None:
        if value < start or end < value:
            return

        self.tree[node] += cnt
        if start != end:
            mid: int = (start + end) // 2
            self.update(2 * node, start, mid, value, cnt)
            self.update(2 * node + 1, mid + 1, end, value, cnt)


if __name__ == "__main__":
    n = int(input())

    stree = SegmentTree()
    for _ in range(n):
        a, *bc = map(int, input().split())
        if a == 1:
            print(stree.get(1, 0, FLAVOR - 1, *bc))
        else:
            stree.update(1, 0, FLAVOR - 1, *bc)
