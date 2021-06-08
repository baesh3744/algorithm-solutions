def analyze_commands(p: str, n: int) -> tuple[int, int, int]:
    is_reversed: bool = False
    start_idx: int = 0
    end_idx: int = n - 1

    for cmd in p:
        if cmd == 'R':
            is_reversed = not is_reversed
        else:
            if not is_reversed:
                start_idx += 1
            else:
                end_idx -= 1

    return start_idx, end_idx, is_reversed


def main() -> None:
    t = int(input())

    for _ in range(t):
        p = input()
        n = int(input())
        arr = input()

        start_idx, end_idx, is_reversed = analyze_commands(p, n)

        if start_idx > end_idx + 1:
            print('error')
        else:
            splitted_arr: list[str] = (
                arr[1:-1].split(',')[start_idx: end_idx + 1])
            if is_reversed:
                splitted_arr.reverse()
            print('[' + ','.join(splitted_arr) + ']')


if __name__ == "__main__":
    main()
