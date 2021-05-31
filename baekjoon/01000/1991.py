from typing import Optional


class Node:
    def __init__(self, data: str):
        self.data: str = data
        self.left: Optional[Node] = None
        self.right: Optional[Node] = None


class BinaryTree:
    def __init__(self):
        self.root: Optional[Node] = None

    def preorder_traversal(self, node: Node) -> str:
        preorder: str = node.data
        if node.left is not None:
            preorder += self.preorder_traversal(node.left)
        if node.right is not None:
            preorder += self.preorder_traversal(node.right)
        return preorder

    def inorder_traversal(self, node: Node) -> str:
        inorder: str = ''
        if node.left is not None:
            inorder += self.inorder_traversal(node.left)
        inorder += node.data
        if node.right is not None:
            inorder += self.inorder_traversal(node.right)
        return inorder

    def postorder_traversal(self, node: Node) -> str:
        postorder: str = ''
        if node.left is not None:
            postorder += self.postorder_traversal(node.left)
        if node.right is not None:
            postorder += self.postorder_traversal(node.right)
        postorder += node.data
        return postorder

    def make_tree(self, node: Node, left_node: Node, right_node: Node) -> None:
        if self.root is None:
            self.root = node
        if not left_node.data == '.':
            node.left = left_node
        if not right_node.data == '.':
            node.right = right_node


def make_nodes(n: int) -> dict[str, Node]:
    nodes: dict[str, Node] = {'.': Node('')}
    for node_num in range(n):
        data: str = chr(65 + node_num)
        nodes[data] = Node(data)
    return nodes


def main() -> None:
    n = int(input())
    nodes = make_nodes(n)
    btree: BinaryTree = BinaryTree()
    for _ in range(n):
        data, left_data, right_data = map(str, input().split())
        btree.make_tree(nodes[data], nodes[left_data], nodes[right_data])

    print(btree.preorder_traversal(btree.root))
    print(btree.inorder_traversal(btree.root))
    print(btree.postorder_traversal(btree.root))


if __name__ == "__main__":
    main()
