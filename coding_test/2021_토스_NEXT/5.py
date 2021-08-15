from typing import List


class SegmentTree:
    def __init__(self, n: int, data: List[int]) -> None:
        self.data = data
        self.tree = [-1 for _ in range(4 * n)]
        self.init(1, 0, n - 1)

    def init(self, node: int, start: int, end: int) -> int:
        if start == end:
            self.tree[node] = self.data[start]
            return self.tree[node]

        mid = (start + end) // 2
        self.tree[node] = max(
            self.init(2 * node, start, mid), self.init(2 * node + 1, mid + 1, end)
        )
        return self.tree[node]

    def max_(self, node: int, start: int, end: int, left: int, right: int) -> int:
        if right < start or end < left:
            return 0
        if left <= start and end <= right:
            return self.tree[node]

        mid = (start + end) // 2
        return max(
            self.max_(2 * node, start, mid, left, right),
            self.max_(2 * node + 1, mid + 1, end, left, right),
        )


def solution(fruitWeights: List[int], k: int) -> List[int]:
    answer: set[int] = set()
    length: int = len(fruitWeights)
    tree: SegmentTree = SegmentTree(length, fruitWeights)
    for start in range(length - k + 1):
        answer.add(tree.max_(1, 0, length - 1, start, start + k - 1))
    return sorted(answer, reverse=True)


print(solution([30, 40, 10, 20, 30], 3))
