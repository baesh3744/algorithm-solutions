import sys
from typing import Optional


class Node:
    def __init__(self, data: int) -> None:
        self.data: int = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    def __init__(self) -> None:
        self.root: Optional[Node] = None
        self.shape: list[list[int]] = []
        self.order: int = 1

    def add_node(self,
                 node: Node,
                 left_node: Optional[Node],
                 right_node: Optional[Node]) -> None:
        node.left = left_node
        node.right = right_node

    def inorder_traversal(self, node: Node, depth: int) -> None:
        if node.left is not None:
            self.inorder_traversal(node.left, depth + 1)

        while len(self.shape) <= depth:
            self.shape.append([])
        if len(self.shape[depth]) == 0:
            self.shape[depth].extend([self.order, self.order])
        else:
            self.shape[depth][1] = self.order
        self.order += 1

        if node.right is not None:
            self.inorder_traversal(node.right, depth + 1)

    def get_widest(self) -> tuple[int, int]:
        level: int = 0
        width: int = 0
        for cur_level in range(1, len(self.shape)):
            cur_width: int = self.shape[cur_level][1] - \
                self.shape[cur_level][0] + 1
            if cur_width > width:
                level = cur_level
                width = cur_width
        return level, width


def make_binary_tree(n: int) -> BinaryTree:
    nodes: list[Node] = [Node(data) for data in range(n + 1)]
    btree: BinaryTree = BinaryTree()
    cnode_sum: int = 0

    for _ in range(n):
        data, left_data, right_data = map(int, sys.stdin.readline().split())

        left_node: Optional[Node] = None
        if left_data != -1:
            left_node = nodes[left_data]
            cnode_sum += left_data
        right_node: Optional[Node] = None
        if right_data != -1:
            right_node = nodes[right_data]
            cnode_sum += right_data

        btree.add_node(nodes[data], left_node, right_node)

    btree.root = nodes[(n * (n + 1) // 2) - cnode_sum]

    return btree


def main() -> None:
    n = int(input())
    btree = make_binary_tree(n)

    btree.inorder_traversal(btree.root, 1)
    level, width = btree.get_widest()
    print(level, width)


if __name__ == "__main__":
    main()
