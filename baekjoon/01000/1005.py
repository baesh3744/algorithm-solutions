import sys


input = sys.stdin.readline

cache: list[int]
times: list[int]
previous: list[list[int]]


def get_time(building: int) -> int:
    if cache[building] != -1:
        return cache[building]

    max_time = 0
    for prev in previous[building]:
        max_time = max(max_time,
                       get_time(prev))
    cache[building] = times[building] + max_time
    return cache[building]


def main() -> None:
    global cache, times, previous
    t = int(input())
    for _ in range(t):
        n, k = map(int, input().split())
        times = [-1] + list(map(int, input().split()))
        previous = [[] for _ in range(n + 1)]
        for _ in range(k):
            x, y = map(int, input().split())
            previous[y].append(x)
        w = int(input())

        cache = [-1 for _ in range(n + 1)]
        print(get_time(w))


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
