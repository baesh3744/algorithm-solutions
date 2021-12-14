import sys
from collections import deque
from typing import List, Tuple, Deque


INF = sys.maxsize

input = sys.stdin.readline


def bfs() -> None:
    que: Deque[int] = deque()

    for a, ismatched in enumerate(matched):
        if ismatched:
            levels[a] = INF
        else:
            levels[a] = 0
            que.append(a)

    while que:
        a = que.popleft()
        for b, _ in adjs[a]:
            if B[b] != -1 and levels[B[b]] == INF:
                levels[B[b]] = levels[a] + 1
                que.append(B[b])


def dfs(a: int, cost: int) -> bool:
    for b, pivot in adjs[a]:
        if pivot <= cost and (
            B[b] == -1 or (levels[B[b]] == levels[a] + 1 and dfs(B[b], cost))
        ):
            matched[a] = True
            B[b] = a
            A[a] = b
            return True
    return False


def hopcroft_karp(cost: int) -> int:
    global A, B, matched, levels
    matching: int = 0
    levels = [INF for _ in range(n)]
    matched = [False for _ in range(n)]
    A = [-1 for _ in range(n)]
    B = [-1 for _ in range(2 * n + 1)]

    while True:
        bfs()

        flow: int = 0
        for a, ismatched in enumerate(matched):
            if not ismatched and dfs(a, cost):
                flow += 1

        if flow == 0:
            break

        matching += flow

    return matching


def getcost() -> int:
    start: int = 0
    end: int = 1000000

    while start <= end:
        mid: int = (start + end) // 2

        if hopcroft_karp(mid) >= n:
            end = mid - 1
        else:
            start = mid + 1

    return start


if __name__ == "__main__":
    n = int(input())

    adjs: List[List[Tuple[int, int]]] = []
    for _ in range(n):
        a0, k0, a1, k1 = map(int, input().split())
        adjs.append([(a0, k0), (a1, k1)])

    print(getcost())
