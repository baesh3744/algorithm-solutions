import sys
from collections import deque


input = sys.stdin.readline


def get_sequence(
    indegree_list: list[int], edge_list: list[tuple[int, int]]
) -> list[int]:
    que: deque[int] = deque()
    seq: list[int] = []

    for node, indegree in enumerate(indegree_list):
        if indegree == 0:
            que.append(node)

    while que:
        cur = que.popleft()
        seq.append(cur + 1)

        for next in edge_list[cur]:
            indegree_list[next] -= 1
            if indegree_list[next] == 0:
                que.append(next)

    return seq


def main() -> None:
    n, m = map(int, input().split())

    indegree_list: list[int] = [0 for _ in range(n)]
    edge_list: list[list[int]] = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(lambda x: int(x) - 1, input().split())
        edge_list[a].append(b)
        indegree_list[b] += 1

    print(" ".join(map(str, get_sequence(indegree_list, edge_list))))


if __name__ == "__main__":
    main()
