import sys


def main() -> None:
    n = int(input())
    toys: list[tuple[float, int, int]] = []
    for toy_index in range(n):
        joy, price = map(int, sys.stdin.readline().split())
        toys.append((joy / price, price, toy_index + 1))
    toys.sort(reverse=True)

    print(sum(map(lambda x: x[1], toys[:3])))
    for toy_index in range(3):
        print(toys[toy_index][2])


if __name__ == "__main__":
    main()
