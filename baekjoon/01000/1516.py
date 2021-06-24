import sys


def get_build_time(building: int) -> int:
    if cache[building] != -1:
        return cache[building]

    time: int = 0
    for idx, prev_building in enumerate(buildings[building - 1]):
        if idx == 0 or prev_building == -1:
            continue
        time = max(time, get_build_time(prev_building))
    cache[building] = time + buildings[building - 1][0]

    return cache[building]


def main() -> None:
    global n, buildings, cache
    n = int(input())
    buildings = [list(map(int, sys.stdin.readline().split()))
                 for _ in range(n)]

    cache = [-1 for _ in range(n + 1)]
    for building in range(1, n + 1):
        get_build_time(building)

    print('\n'.join(map(str, cache[1:])))


if __name__ == "__main__":
    main()
