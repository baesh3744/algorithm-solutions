import sys


input = sys.stdin.readline


def get_energy(stone: int, very_big: int) -> int:
    if stone == 0:
        return 0
    if cache[stone][very_big] != -1:
        return cache[stone][very_big]

    energy = sys.maxsize
    if stone - 3 >= 0 and very_big == 1:
        energy = min(energy, get_energy(stone - 3, 0) + k)
    if stone - 2 >= 0:
        energy = min(energy, get_energy(stone - 2, very_big) + big_list[stone - 2])
    if stone - 1 >= 0:
        energy = min(energy, get_energy(stone - 1, very_big) + small_list[stone - 1])
    return energy


def main() -> None:
    global k, small_list, big_list, cache
    n = int(input())

    small_list = [-1 for _ in range(n - 1)]
    big_list = [-1 for _ in range(n - 1)]
    for index in range(n - 1):
        small, big = map(int, input().split())
        small_list[index] = small
        big_list[index] = big
    k = int(input())

    cache = [[-1 for _ in range(2)] for _ in range(n)]
    print(get_energy(n-1, 1))


if __name__ == "__main__":
    main()
