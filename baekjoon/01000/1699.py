import math


def main() -> None:
    n = int(input())

    cache = [num for num in range(n + 1)]
    for num in range(1, n + 1):
        for sqrt in range(1, math.floor(math.sqrt(num)) + 1):
            cache[num] = min(cache[num], 1 + cache[num - sqrt * sqrt])
    print(cache[n])


if __name__ == "__main__":
    main()
