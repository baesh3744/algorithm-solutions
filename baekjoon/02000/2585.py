import math
import sys

input = sys.stdin.readline


def make_distance_board(n: int, landings: list[list[int]]) -> list[list[int]]:
    landings.insert(0, [0, 0])
    landings.append([10000, 10000])

    board = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for start_apt in range(n+2):
        for end_apt in range(start_apt+1, n+2):
            start_x, start_y = landings[start_apt]
            end_x, end_y = landings[end_apt]

            dist = (start_x-end_x) ** 2 + (start_y-end_y) ** 2
            fuel = math.ceil(math.sqrt(dist) / 10)

            board[start_apt][end_apt] = fuel
            board[end_apt][start_apt] = fuel
    return board


def count_landing(n: int, dist: int, land: int, visited: list[bool]) -> int:
    if land == n+1:
        return -1
    if cache[land] != -1:
        return cache[land]

    cnt_landing = sys.maxsize
    for next_land in range(1, n+2):
        if board[land][next_land] <= dist and not visited[next_land]:
            visited[next_land] = True
            cnt_landing = min(cnt_landing,
                              count_landing(n, dist, next_land, visited) + 1)
            visited[next_land] = False
    cache[land] = cnt_landing
    return cache[land]


def get_min_fuel_capacity(n: int, k: int) -> int:
    global cache
    left, right = 0, 1500
    while left <= right:
        mid = (left + right) // 2
        cache = [-1 for _ in range(n+2)]

        cnt_landing = count_landing(n, mid, 0, [False] * (n+2))

        if cnt_landing == sys.maxsize or cnt_landing > k:
            left = mid + 1
        else:
            right = mid - 1
    return left


def main() -> None:
    global board
    n, k = map(int, input().split())
    landings = [list(map(int, input().split())) for _ in range(n)]

    board = make_distance_board(n, landings)
    print(get_min_fuel_capacity(n, k))


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
