import sys
from collections import deque
from itertools import chain, product
from typing import Deque, List


Land = List[List[int]]
Tree = List[List[Deque[int]]]

moves: List[int] = [-1, 0, 1]


def count_tree_after_year(n: int,
                          k: int,
                          land: Land,
                          trees: Tree,
                          nourishment: Land) -> int:

    for _ in range(k):
        new_trees: Land = [[0 for _ in range(n)] for _ in range(n)]

        # Spring + Summer + Winter
        for x in range(n):
            for y in range(n):
                dead_tree: int = 0
                alive_trees: Deque[int] = deque()
                for age in trees[x][y]:
                    if land[x][y] < age:
                        dead_tree += age // 2
                    else:
                        land[x][y] -= age
                        alive_trees.append(age + 1)

                        if (age + 1) % 5 == 0:
                            new_trees[x][y] += 1

                land[x][y] += dead_tree + nourishment[x][y]
                trees[x][y] = alive_trees

        # Fall
        for x in range(n):
            for y in range(n):
                if new_trees[x][y] != 0:
                    for move_x, move_y in product(moves, moves):
                        if move_x == 0 and move_y == 0:
                            continue

                        next_x, next_y = x + move_x, y + move_y
                        if 0 <= next_x < n and 0 <= next_y < n:
                            trees[next_x][next_y].extendleft(
                                [1] * new_trees[x][y])

    cnt_tree: int = 0
    for tree in chain.from_iterable(trees):
        cnt_tree += len(tree)
    return cnt_tree


def main() -> None:
    n, m, k = map(int, input().split())
    nourishment = [list(map(int, input().split())) for _ in range(n)]

    trees: Tree = [[deque() for _ in range(n)] for _ in range(n)]
    for _ in range(m):
        x, y, z = map(int, sys.stdin.readline().split())
        trees[x - 1][y - 1].append(z)

    land = [[5 for _ in range(n)] for _ in range(n)]
    print(count_tree_after_year(n, k, land, trees, nourishment))


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
