board: list[int] = [
    0, 2, 4, 6, 8,
    10, 12, 14, 16, 18,
    20, 22, 24, 26, 28,
    30, 32, 34, 36, 38,
    40, 0, 13, 16, 19,
    25, 22, 24, 28, 27,
    26, 30, 35
]
first_loc: dict[int, int] = {5: 22, 10: 26, 15: 28}
jump_loc: dict[int, int] = {25: 31, 27: 25, 30: 25, 32: 20}


def get_next_loc(cur_loc: int, dice: int) -> int:
    next_loc: int = cur_loc
    for midx in range(dice):
        if next_loc == 21:
            break
        elif midx == 0 and next_loc in first_loc:
            next_loc = first_loc[next_loc]
        elif next_loc in jump_loc:
            next_loc = jump_loc[next_loc]
        else:
            next_loc += 1
    return next_loc


def move(turn: int, score: int, horses: list[int]) -> int:
    if turn == 10:
        return score

    max_score: int = 0
    for hidx, horse in enumerate(horses):
        next_horse: int = get_next_loc(horse, moves[turn])

        can_move: bool = True
        for value in horses:
            if value == next_horse and value != 21:
                can_move = False

        if can_move:
            horses[hidx] = next_horse
            max_score = max(max_score,
                            move(turn + 1, score + board[next_horse], horses))
            horses[hidx] = horse

    return max_score


def main() -> None:
    global moves
    moves = list(map(int, input().split()))

    print(move(0, 0, [0, 0, 0, 0]))


if __name__ == "__main__":
    main()
