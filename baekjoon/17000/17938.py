def get_hand_location(n: int, t: int) -> tuple[int, int]:
    start, cnt_hand, hand_diff = 0, 1, 1
    for _ in range(t - 1):
        start += cnt_hand
        if cnt_hand == 2*n:
            hand_diff = -1
        elif cnt_hand == 1:
            hand_diff = 1
        cnt_hand += hand_diff
    return start % (2*n), (start + cnt_hand - 1) % (2*n)


def main() -> None:
    n = int(input())
    p, t = map(int, input().split())

    start, last = get_hand_location(n, t)

    can_troll: bool = False
    num: int = start
    while num != last:
        if num == 2 * (p-1) or num == 2*p - 1:
            can_troll = True
            break
        num += 1
        if num == 2 * n:
            num = 0
    if last == 2 * (p-1) or last == 2*p - 1:
        can_troll = True

    if can_troll and not (start <= last and start // 2 == last // 2):
        print('Dehet YeonJwaJe ^~^')
    else:
        print('Hing...NoJam')


if __name__ == "__main__":
    main()
