import math


def main() -> None:
    _ = int(input())
    radius_list = list(map(int, input().split()))

    for radius in radius_list[1:]:
        gcd_ = math.gcd(radius_list[0], radius)
        print(f"{radius_list[0] // gcd_}/{radius // gcd_}")


if __name__ == "__main__":
    main()
