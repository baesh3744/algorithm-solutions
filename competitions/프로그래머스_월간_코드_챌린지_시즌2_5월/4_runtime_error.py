from typing import Dict, List


def make_parent_links(n: int, edges: List[List[int]]) -> Dict[int, int]:
    parent_dict: Dict[int, int] = {node: 0 for node in range(1, n + 1)}
    for parent, child in edges:
        parent_dict[child] = parent
    return parent_dict


def make_children_links(n: int, edges: List[List[int]]) -> Dict[int, List[int]]:
    children_dict: Dict[int, List[int]] = {
        node: [] for node in range(1, n + 1)}
    for parent, child in edges:
        children_dict[parent].append(child)
    return children_dict


def make_tree(node: int, values: List[int]) -> None:
    tree[node] = values[node - 1]
    for child in children_dict[node]:
        make_tree(child, values)
        tree[node] += tree[child]


def get_node_value(node: int) -> int:
    children_sum: int = 0
    for child in children_dict[node]:
        children_sum += tree[child]
    return tree[node] - children_sum


def update_tree(node: int, w: int) -> None:
    global tree
    if node == 1:
        node_value = get_node_value(node)
        tree[node] += w - node_value
    else:
        parent_value: int = get_node_value(parent_dict[node])
        node_value = get_node_value(node)
        tree[node] += parent_value - node_value
        update_tree(parent_dict[node], w)


def solution(values: List[int], edges: List[List[int]], queries: List[List[int]]) -> List[int]:
    global parent_dict, children_dict, tree
    answer: List[int] = []
    n: int = len(values)
    tree = [0 for _ in range(n + 1)]
    parent_dict = make_parent_links(n, edges)
    children_dict = make_children_links(n, edges)
    make_tree(1, values)

    for u, w in queries:
        if w == -1:
            answer.append(tree[u])
        else:
            update_tree(u, w)

    return answer


print(solution([1, 10, 100, 1000, 10000],
               [[1, 2], [1, 3], [2, 4], [2, 5]],
               [[1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [4, 1000], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1], [2, 1], [1, -1], [2, -1], [3, -1], [4, -1], [5, -1]]))
# [11111,11010,100,1000,10000,11111,10011,100,10,10000,11111,11010,100,10,10000]
