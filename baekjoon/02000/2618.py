import sys


Point = tuple[int, int]

INIT: int = 0
INITIAL_DISTANCE: int = sys.maxsize

input = sys.stdin.readline


def get_distance(_from: int, _to: int) -> int:
    if distances[_from][_to] != INITIAL_DISTANCE:
        return distances[_from][_to]

    frow, fcol = accidents[_from]
    trow, tcol = accidents[_to]
    dist = abs(frow - trow) + abs(fcol - tcol)
    distances[_from][_to] = distances[_to][_from] = dist
    return dist


def move(car1: int, car2: int, acc_number: int) -> int:
    if acc_number == w + 2:
        return 0
    if cache[car1][car2] != INIT:
        return cache[car1][car2]

    move_car1 = move(acc_number, car2, acc_number + 1) + get_distance(car1, acc_number)
    move_car2 = move(car1, acc_number, acc_number + 1) + get_distance(car2, acc_number)
    cache[car1][car2] = min(move_car1, move_car2)
    return cache[car1][car2]


def track(car1: int, car2: int, acc_number: int) -> None:
    if acc_number == w + 2:
        return

    move_car1 = cache[acc_number][car2] + get_distance(car1, acc_number)
    if cache[car1][car2] == move_car1:
        result[acc_number] = 1
        track(acc_number, car2, acc_number + 1)
    else:
        result[acc_number] = 2
        track(car1, acc_number, acc_number + 1)


def main() -> None:
    global n, w, accidents, cache, result, distances
    n = int(input())
    w = int(input())
    accidents = [Point((1, 1)), Point((n, n))] + (
        [Point(map(int, input().split())) for _ in range(w)]
    )

    cache = [[INIT for _ in range(w + 2)] for _ in range(w + 2)]
    distances = [[INITIAL_DISTANCE for _ in range(w + 2)] for _ in range(w + 2)]
    result = [-1 for _ in range(w + 2)]
    print(move(0, 1, 2))
    track(0, 1, 2)
    for car in result[2:]:
        print(car)


if __name__ == "__main__":
    sys.setrecursionlimit(2000)
    main()
