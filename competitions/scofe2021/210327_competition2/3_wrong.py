from typing import List


tree: List[List[int]] = []
child_map: List[List[bool]] = []


def add_children(node: int) -> None:
    for child in tree[node]:
        if len(tree[child]) != 0:
            add_children(child)

        tree[node] += tree[child]
        child_map[node][child] = True
        for n in tree[child]:
            child_map[node][n] = True


def main() -> None:
    global tree
    N, Q = map(int, input().split())

    for _ in range(N + 1):
        tree.append([])
        child_map.append([False for _ in range(N + 1)])

    root: int = 0
    for idx in range(N - 1):
        upper, down = map(int, input().split())
        tree[upper].append(down)

        if idx == 0 or root == down:
            root = upper

    add_children(root)

    for _ in range(Q):
        upper, down = map(int, input().split())
        print('yes' if child_map[upper][down] else 'no')


if __name__ == "__main__":
    main()
