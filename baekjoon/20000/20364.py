import sys


input = sys.stdin.readline


def find(tree: list[bool], land: int) -> int:
    first: int = 0
    while land > 0:
        if tree[land]:
            first = land
        land //= 2
    return first


def main() -> None:
    n, q = map(int, input().split())

    tree: list[bool] = [False for _ in range(n + 1)]
    for _ in range(q):
        land = int(input())
        first = find(tree, land)
        tree[land] = True
        print(first)


if __name__ == "__main__":
    main()
