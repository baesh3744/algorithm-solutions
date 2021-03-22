from typing import List


MAX: int = 100
MOVE: List[List[int]] = [[-1, 0], [0, 1], [1, 0], [0, -1]]


def find_coin() -> List[List[int]]:
    coins: List[List[int]] = []
    for row_index, row in enumerate(board):
        for col_index, status in enumerate(row):
            if status == 'o':
                coins.append([row_index, col_index])
    return coins


def is_range(coin: List[int]) -> bool:
    return 0 <= coin[0] < N and 0 <= coin[1] < M


def press_button(coins: List[List[int]], count: int) -> int:
    if count >= 10:
        return MAX

    ret: int = MAX
    for move in MOVE:
        new_coins: List[List[int]] = []
        new_count: int = count + 1
        out_of_range: int = 0

        for coin in coins:
            new_coin: List[int] = [coin[idx] + move[idx] for idx in range(2)]

            if not is_range(new_coin):
                out_of_range += 1
            else:
                new_coins.append(
                    new_coin) if board[new_coin[0]][new_coin[1]] != '#' else new_coins.append(coin)

        if out_of_range == 0:
            ret = min(ret, press_button(new_coins, new_count))
        elif out_of_range == 1:
            return new_count
    return ret


def main() -> None:
    global N, M, board
    N, M = map(int, input().split())
    board = [[ch for ch in input()] for _ in range(N)]

    coins: List[List[int]] = find_coin()
    count: int = press_button(coins, 0)
    print(count if count != MAX else -1)


if __name__ == "__main__":
    main()
