def count_lan(lans: list[int], length: int) -> int:
    cnt_lan: int = 0
    for lan in lans:
        cnt_lan += (lan // length)
    return cnt_lan


def get_max_lan_length(lans: list[int], n: int) -> int:
    left: int = 1
    right: int = max(lans)

    while left <= right:
        mid: int = (left + right) // 2

        cnt_lan = count_lan(lans, mid)

        if n <= cnt_lan:
            left = mid + 1
        else:
            right = mid - 1

    return right


def main() -> None:
    k, n = map(int, input().split())
    lans = [int(input()) for _ in range(k)]

    print(get_max_lan_length(lans, n))


if __name__ == "__main__":
    main()
