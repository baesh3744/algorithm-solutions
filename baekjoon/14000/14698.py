import sys
from heapq import heapify, heappop, heappush


MOD = 1000000007

input = sys.stdin.readline


def get_energy(n: int, slimes: list[int]) -> int:
    energy: int = 1
    heap: list[int] = slimes

    heapify(heap)
    for _ in range(n - 1):
        first: int = heappop(heap)
        second: int = heappop(heap)
        new_slime: int = first * second
        energy *= new_slime
        heappush(heap, new_slime)

    return energy % MOD


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        slimes = list(map(int, input().split()))
        print(get_energy(n, slimes))
