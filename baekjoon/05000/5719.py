import heapq
import sys


PathList = list[list[tuple[int, int]]]

MAX: int = sys.maxsize

input = sys.stdin.readline


def dijkstra(n: int, start: int, path_list: PathList) -> list[int]:
    distances: list[int] = [MAX for _ in range(n)]
    heap: list[tuple[int, int]] = []

    distances[start] = 0
    heapq.heappush(heap, (0, start))

    while heap:
        dist, node = heapq.heappop(heap)
        if dist > distances[node]:
            continue

        for adj_node, adj_dist in path_list[node]:
            next_dist: int = dist + adj_dist
            if next_dist < distances[adj_node]:
                distances[adj_node] = next_dist
                heapq.heappush(heap, (next_dist, adj_node))

    return distances


def remove_path(
    dpt: int, path_list: PathList, dists_from_s: list[int], dists_from_d: list[int]
) -> PathList:
    for _from, paths in enumerate(path_list):
        for idx, (_to, dist) in enumerate(paths):
            if dists_from_s[_from] + dist + dists_from_d[_to] == dists_from_s[dpt]:
                path_list[_from][idx] = (_to, MAX)
    return path_list


def main() -> None:
    while True:
        n, m = map(int, input().split())
        if n == 0 and m == 0:
            break
        s, d = map(int, input().split())

        path_list: PathList = [[] for _ in range(n)]
        tracking_list: PathList = [[] for _ in range(n)]
        for _ in range(m):
            u, v, p = map(int, input().split())
            path_list[u].append((v, p))
            tracking_list[v].append((u, p))

        dists_from_s = dijkstra(n, s, path_list)
        dists_from_d = dijkstra(n, d, tracking_list)
        path_list = remove_path(d, path_list, dists_from_s, dists_from_d)
        distances = dijkstra(n, s, path_list)
        print(distances[d] if distances[d] != MAX else -1)


if __name__ == "__main__":
    main()
