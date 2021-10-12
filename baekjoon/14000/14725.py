import sys


input = sys.stdin.readline


class Node:
    def __init__(self, value: str) -> None:
        self.value = value
        self.children: list[Node] = []

class Tree:
    def __init__(self) -> None:
        self.root = Node('')

    def add(self, node: Node, value_list: list[str]) -> None:
        if not value_list:
            return
        for child in node.children:
            if child.value == value_list[0]:
                self.add(child, value_list[1:])
                return
        next_node = Node(value_list[0])
        node.children.append(next_node)
        self.add(next_node, value_list[1:])

    def print_structure(self, node: Node, depth: int) -> None:
        if node != self.root:
            print(depth * '--' + node.value)
        for child in sorted(node.children, key=lambda x: x.value):
            self.print_structure(child, depth + 1)


def main() -> None:
    n = int(input())

    tree = Tree()
    for _ in range(n):
        value_list = list(input().split())
        tree.add(tree.root, value_list[1:])

    tree.print_structure(tree.root, -1)


if __name__ == "__main__":
    main()
