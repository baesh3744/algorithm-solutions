import sys


input = sys.stdin.readline


def count(city: int, is_selected: int) -> int:
    if cache[city][is_selected] != -1:
        return cache[city][is_selected]

    cnt: int = is_selected * numbers[city]
    for adj_city in adj_list[city]:
        if visited[adj_city]:
            continue

        visited[city] = True

        adj_cnt: int = count(adj_city, 0)
        if is_selected == 0:
            adj_cnt = max(adj_cnt, count(adj_city, 1))
        cnt += adj_cnt

        visited[city] = False

    cache[city][is_selected] = cnt
    return cache[city][is_selected]


if __name__ == "__main__":
    sys.setrecursionlimit(20000)

    n = int(input())
    numbers = list(map(int, input().split()))

    adj_list: list[list[int]] = [[] for _ in range(n)]
    for _ in range(n - 1):
        city1, city2 = map(lambda x: int(x) - 1, input().split())
        adj_list[city1].append(city2)
        adj_list[city2].append(city1)

    cache: list[list[int]] = [[-1 for _ in range(2)] for _ in range(n)]
    visited: list[bool] = [False for _ in range(n)]
    visited[0] = True
    print(max(count(0, 0), count(0, 1)))
