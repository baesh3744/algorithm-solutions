def get_expected_value(a: int, d: float, k: float) -> float:
    time = a
    evalue, rate = 0.0, 1.0
    while rate > 0:
        evalue += time * rate * min(d, 1.0)
        rate *= 1 - d
        d *= 1 + k
        time += a
    return evalue


def main() -> None:
    a, d, k = map(int, input().split())

    print("%.7f" % get_expected_value(a, d / 100, k / 100))


if __name__ == "__main__":
    main()
