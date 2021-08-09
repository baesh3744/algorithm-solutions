import math


def main() -> None:
    t = int(input())
    for _ in range(t):
        x1, y1, r1, x2, y2, r2 = map(float, input().split())

        jo2baek = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        if jo2baek == 0.0 and r1 == r2:
            print(-1)
            continue

        bigger, smaller = max(r1, r2), min(r1, r2)
        if bigger > smaller + jo2baek or jo2baek > bigger + smaller:
            print(0)
        elif bigger == smaller + jo2baek or jo2baek == bigger + smaller:
            print(1)
        else:
            print(2)


if __name__ == "__main__":
    main()
