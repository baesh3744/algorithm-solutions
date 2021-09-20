import sys


input = sys.stdin.readline


def eat(n: int, foods: list[int]) -> int:
    cache = [[0 for _ in range(3)] for _ in range(n)]
    cache[0][1] = foods[0]
    for corner in range(1, n):
        cache[corner][0] = max(cache[corner - 1])
        cache[corner][1] = cache[corner - 1][0] + foods[corner]
        cache[corner][2] = cache[corner - 1][1] + foods[corner] // 2
    return max(cache[n - 1])


def main() -> None:
    n = int(input())
    foods = [int(input()) for _ in range(n)]
    print(eat(n, foods))


if __name__ == "__main__":
    main()
