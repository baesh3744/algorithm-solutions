import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, n: int, data: list[int]) -> None:
        self.data = data
        self.tree: list[int] = [0 for _ in range(4 * n)]
        self.__initialize(1, 0, n-1)

    def __initialize(self, node: int, start: int, end: int) -> int:
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = self.__initialize(2*node, start, mid) \
            + self.__initialize(2*node+1, mid+1, end)
        return self.tree[node]

    def sum_(self, node: int, start: int, end: int,
             left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return self.sum_(2*node, start, mid, left, right) \
            + self.sum_(2*node+1, mid+1, end, left, right)

    def update(self, node: int, start: int, end: int,
               index: int, diff: int) -> None:
        if index < start or end < index:
            return

        self.tree[node] += diff
        if start != end:
            mid = (start + end) // 2
            self.update(2*node, start, mid, index, diff)
            self.update(2*node+1, mid+1, end, index, diff)


def main() -> None:
    n, m, k = map(int, input().split())
    data = [int(input()) for _ in range(n)]

    segment_tree = SegmentTree(n, data)
    for _ in range(m + k):
        a, b, c = map(int, input().split())
        if a == 1:
            diff = c - segment_tree.data[b-1]
            segment_tree.update(1, 0, n-1, b-1, diff)
            segment_tree.data[b-1] = c
        else:
            print(segment_tree.sum_(1, 0, n-1, b-1, c-1))


if __name__ == "__main__":
    main()
