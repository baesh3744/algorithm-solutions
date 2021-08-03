import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, n: int, data: list[int]) -> None:
        self.data = data
        self.tree: list[tuple[int, int]] = [(0, 0) for _ in range(4 * n)]
        self.__initialize(1, 0, n-1)

    def __initialize(self, node: int, start: int, end: int) -> tuple[int, int]:
        if start == end:
            self.tree[node] = self.data[start], self.data[start]
            return self.tree[node]

        mid = (start + end) // 2
        min_lnode, max_lnode = self.__initialize(2*node, start, mid)
        min_rnode, max_rnode = self.__initialize(2*node+1, mid+1, end)
        self.tree[node] = min(min_lnode, min_rnode), max(max_lnode, max_rnode)
        return self.tree[node]

    def get(self, node: int, start: int, end: int,
            left: int, right: int) -> tuple[int, int]:
        if right < start or end < left:
            return sys.maxsize, -1
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        min_lnode, max_lnode = self.get(2*node, start, mid, left, right)
        min_rnode, max_rnode = self.get(2*node+1, mid+1, end, left, right)
        return min(min_lnode, min_rnode), max(max_lnode, max_rnode)


def main() -> None:
    n, m = map(int, input().split())
    data = [int(input()) for _ in range(n)]

    segment_tree = SegmentTree(n, data)
    for _ in range(m):
        a, b = map(int, input().split())
        print(' '.join(map(str, segment_tree.get(1, 0, n-1, a-1, b-1))))


if __name__ == "__main__":
    main()
