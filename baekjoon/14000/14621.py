import heapq
import sys


input = sys.stdin.readline


def get_distance(n: int, edge_list: list[list[tuple[int, int]]]) -> int:
    distance: int = 0

    start_node: int = 1
    connected: set[int] = set([start_node])
    candidate_edge_list: list[tuple[int, int]] = edge_list[start_node]
    heapq.heapify(candidate_edge_list)

    while candidate_edge_list:
        dist, node = heapq.heappop(candidate_edge_list)
        if node not in connected:
            distance += dist
            connected.add(node)
            for next_node in edge_list[node]:
                if next_node not in connected:
                    heapq.heappush(candidate_edge_list, next_node)

    if distance == 0 or len(connected) != n:
        return -1
    return distance


def main() -> None:
    n, m = map(int, input().split())
    type_list = [""] + list(input().split())

    edge_list: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v, d = map(int, input().split())
        if type_list[u] != type_list[v]:
            edge_list[u].append((d, v))
            edge_list[v].append((d, u))

    print(get_distance(n, edge_list))


if __name__ == "__main__":
    main()
