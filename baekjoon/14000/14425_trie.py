import sys
from typing import Union


input = sys.stdin.readline


class Node:
    def __init__(self, key: str) -> None:
        self.key: str = key
        self.data: Union[str, None] = None
        self.children: dict[str, Node] = {}


class Trie:
    def __init__(self) -> None:
        self.root: Node = Node("")

    def insert(self, string: str) -> None:
        node: Node = self.root
        for char in string:
            if char not in node.children:
                node.children[char] = Node(char)
            node = node.children[char]
        node.data = string

    def search(self, string: str) -> bool:
        node: Node = self.root
        for char in string:
            if char not in node.children:
                return False
            node = node.children[char]
        if node.data is None:
            return False
        return True


def main() -> None:
    n, m = map(int, input().split())

    trie: Trie = Trie()
    for _ in range(n):
        trie.insert(input())

    cnt: int = 0
    for _ in range(m):
        if trie.search(input()):
            cnt += 1
    print(cnt)


if __name__ == "__main__":
    main()
