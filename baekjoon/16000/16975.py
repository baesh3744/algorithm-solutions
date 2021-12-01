import sys


input = sys.stdin.readline


class FenwickTree:
    def __init__(self, n: int, a: list[int]) -> None:
        self.n: int = n
        self.tree: list[int] = [0 for _ in range(n + 1)]

        self.update(1, a[0])
        for idx, num in enumerate(a[1:], 2):
            self.update(idx, num - a[idx - 2])

    def sum(self, idx: int) -> int:
        ans: int = 0
        while idx > 0:
            ans += self.tree[idx]
            idx -= idx & -idx
        return ans

    def update(self, idx: int, num: int) -> None:
        while idx <= self.n:
            self.tree[idx] += num
            idx += idx & -idx


if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))

    fwtree: FenwickTree = FenwickTree(n, a)

    m = int(input())
    for _ in range(m):
        case, *query = map(int, input().split())
        if case == 1:
            i, j, k = query
            fwtree.update(i, k)
            fwtree.update(j + 1, -k)
        else:
            print(fwtree.sum(*query))
