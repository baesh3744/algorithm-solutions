import sys


input = sys.stdin.readline


class SegmentTree:
    def __init__(self, n: int, numbers: list[int]) -> None:
        self.numbers = numbers
        self.lazy = [0 for _ in range(4 * n)]
        self.tree = [0 for _ in range(4 * n)]

    def init(self, node: int, start: int, end: int) -> int:
        if start == end:
            self.tree[node] = self.numbers[start]
            return self.tree[node]

        mid: int = (start + end) // 2
        self.tree[node] = self.init(2 * node, start, mid) + self.init(
            2 * node + 1, mid + 1, end
        )
        return self.tree[node]

    def update_lazy(self, node: int, start: int, end: int) -> None:
        if self.lazy[node] != 0:
            self.tree[node] += (end - start + 1) * self.lazy[node]
            if start != end:
                self.lazy[2 * node] += self.lazy[node]
                self.lazy[2 * node + 1] += self.lazy[node]
            self.lazy[node] = 0

    def update(
        self, node: int, start: int, end: int, left: int, right: int, diff: int
    ) -> None:
        self.update_lazy(node, start, end)
        if start > right or end < left:
            return

        # 완전히 포함되는 범위 - 현재 노드 갱신 후, 자식 노드의 lazy 설정
        if left <= start and end <= right:
            self.tree[node] += (end - start + 1) * diff
            if start != end:
                self.lazy[2 * node] += diff
                self.lazy[2 * node + 1] += diff
            return

        # 걸치는 범위
        mid: int = (start + end) // 2
        self.update(2 * node, start, mid, left, right, diff)
        self.update(2 * node + 1, mid + 1, end, left, right, diff)
        self.tree[node] = self.tree[2 * node] + self.tree[2 * node + 1]

    def get_sum(self, node: int, start: int, end: int, left: int, right: int) -> int:
        self.update_lazy(node, start, end)
        if start > right or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]
        mid: int = (start + end) // 2
        return self.get_sum(2 * node, start, mid, left, right) + self.get_sum(
            2 * node + 1, mid + 1, end, left, right
        )


def main() -> None:
    n, m, k = map(int, input().split())

    numbers = [int(input()) for _ in range(n)]
    segment_tree = SegmentTree(n, numbers)
    segment_tree.init(1, 0, n - 1)

    for _ in range(m + k):
        cmd = list(map(int, input().split()))
        if cmd[0] == 1:
            segment_tree.update(1, 0, n - 1, cmd[1] - 1, cmd[2] - 1, cmd[3])
        else:
            print(segment_tree.get_sum(1, 0, n - 1, cmd[1] - 1, cmd[2] - 1))


if __name__ == "__main__":
    main()
