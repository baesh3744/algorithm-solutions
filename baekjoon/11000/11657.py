import sys


MAX = sys.maxsize

input = sys.stdin.readline


def has_cycle(init: int) -> bool:
    time_list[init] = 0

    for _ in range(n - 1):
        for start, end, time in bus_list:
            if time_list[start] != MAX and time_list[start] + time < time_list[end]:
                time_list[end] = time_list[start] + time

    for start, end, time in bus_list:
        if time_list[start] != MAX and time_list[start] + time < time_list[end]:
            return True

    return False


if __name__ == "__main__":
    n, m = map(int, input().split())

    bus_list: list[tuple[int, int, int]] = []
    for _ in range(m):
        a, b, c = map(int, input().split())
        bus_list.append((a, b, c))

    time_list: list[int] = [MAX for _ in range(n + 1)]
    if has_cycle(1):
        print(-1)
    else:
        for time in time_list[2:]:
            print(time if time != MAX else -1)
