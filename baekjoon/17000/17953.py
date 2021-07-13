def get_max_satisfication(n: int, m: int, satis: list[list[int]]) -> int:
    cache = [[-1 for _ in range(m)] for _ in range(n)]

    for dessert in range(m):
        cache[0][dessert] = satis[dessert][0]

    for day in range(1, n):
        for dessert in range(m):
            max_satis: int = -1
            for prev_dessert in range(m):
                today_satis = 0
                if dessert == prev_dessert:
                    today_satis = satis[dessert][day] // 2
                else:
                    today_satis = satis[dessert][day]
                max_satis = max(max_satis,
                                cache[day - 1][prev_dessert] + today_satis)
            cache[day][dessert] = max_satis
    return max(cache[n - 1])


def main() -> None:
    n, m = map(int, input().split())
    satis = [list(map(int, input().split())) for _ in range(m)]
    print(get_max_satisfication(n, m, satis))


if __name__ == "__main__":
    main()
