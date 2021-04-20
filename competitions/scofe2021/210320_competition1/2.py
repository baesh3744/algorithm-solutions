def dp(position: int) -> int:
    if position == 0:
        return 1
    if cache[position] != -1:
        return cache[position]

    ret: int = 0
    for move in range(1, 3):
        next_position: int = position - move
        if 0 <= next_position and path[next_position] == 1:
            ret += dp(next_position)
    cache[position] = ret
    return ret


def main() -> None:
    global path, cache
    N = int(input())
    path = [int(chr) for chr in input()]

    cache = [-1 for _ in range(N)]

    print(dp(N - 1))


if __name__ == "__main__":
    main()
