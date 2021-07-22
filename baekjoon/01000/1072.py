import math


def main() -> None:
    x, y = map(int, input().split())
    rate = y*100 // x
    z = -1
    if rate != 99:
        z = math.ceil((100*y - (rate+1)*x) / (rate-99))
    print(z if 0 < z else -1)


if __name__ == "__main__":
    main()
