import sys
from typing import Optional


class Node:
    def __init__(self, key: str, data: Optional[str] = None):
        self.key: str = key
        self.data: Optional[str] = data
        self.children: dict[str, Node] = {}


class Trie:
    def __init__(self):
        self.head: Node = Node('')

    def insert(self, string: str):
        cur_node: Node = self.head
        for ch in string:
            if ch not in cur_node.children:
                cur_node.children[ch] = Node(ch)
            cur_node = cur_node.children[ch]
        cur_node.data = string

    def search(self, node: Node):
        if node.data is not None and len(node.children) != 0:
            return False
        for child in node.children.values():
            if not self.search(child):
                return False
        return True


def main() -> None:
    t = int(input())
    for _ in range(t):
        n = int(sys.stdin.readline())

        trie: Trie = Trie()
        for _ in range(n):
            trie.insert(sys.stdin.readline().strip())
        print('YES' if trie.search(trie.head) else 'NO')


if __name__ == "__main__":
    main()
