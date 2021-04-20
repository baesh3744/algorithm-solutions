def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1


def make_set(node):
    parent[node] = node
    rank[node] = 0


def kruskal(graph) -> int:
    min_weight: int = 0

    for node in graph['vertices']:
        make_set(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            min_weight += weight

    return min_weight


def make_graph(inputs):
    graph = {'vertices': [], 'edges': []}

    for input in inputs:
        node1, node2, weight = input
        if not node1 in graph['vertices']:
            graph['vertices'].append(node1)
        if not node2 in graph['vertices']:
            graph['vertices'].append(node2)
        graph['edges'].append((int(weight), node1, node2))
    return graph


def main() -> None:
    global parent, rank
    N = int(input())
    inputs = [list(map(str, input().split())) for _ in range(N)]

    parent = dict()
    rank = dict()
    print(kruskal(make_graph(inputs)))


if __name__ == "__main__":
    main()
