import sys
from heapq import heappop, heappush


MAX = sys.maxsize

input = sys.stdin.readline


def dijkstra(n: int, start: int, adjs: list[list[tuple[int, int]]]) -> list[int]:
    times: list[int] = [MAX for _ in range(n + 1)]
    heap: list[tuple[int, int]] = []

    times[start] = 0
    heappush(heap, (0, start))

    while heap:
        time, city = heappop(heap)
        if times[city] < time:
            continue

        for adj_city, adj_time in adjs[city]:
            new_time: int = time + adj_time
            if new_time < times[adj_city]:
                times[adj_city] = new_time
                heappush(heap, (new_time, adj_city))

    return times[1:]


if __name__ == "__main__":
    n, m, x = map(int, input().split())

    paths: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    rpaths: list[list[tuple[int, int]]] = [[] for _ in range(n + 1)]
    for _ in range(m):
        start, end, time = map(int, input().split())
        paths[start].append((end, time))
        rpaths[end].append((start, time))

    go_times = dijkstra(n, x, rpaths)
    comeback_times = dijkstra(n, x, paths)
    print(max(time + rtime for time, rtime in zip(go_times, comeback_times)))
