import copy


Directions = list[int]
Locations = list[tuple[int, int]]
Board = list[list[int]]

EMPTY = (-1, -1)

move_row = [-1, -1, 0, 1, 1, 1, 0, -1]
move_col = [0, -1, -1, -1, 0, 1, 1, 1]


def is_range(ridx: int, cidx: int) -> bool:
    return 0 <= ridx < 4 and 0 <= cidx < 4


def move_fish(fish: int,
              directions: Directions,
              locations: Locations,
              board: Board) -> tuple[Directions, Locations, Board]:
    cur_ridx, cur_cidx = locations[fish]
    cur_dir = directions[fish]
    is_moved = False

    for turn in range(8):
        if is_moved:
            break

        next_dir = (cur_dir + turn) % 8
        next_ridx = cur_ridx + move_row[next_dir]
        next_cidx = cur_cidx + move_col[next_dir]
        if is_range(next_ridx, next_cidx) \
           and locations[0] != (next_ridx, next_cidx):
            swapped = board[next_ridx][next_cidx]
            if swapped != -1:
                locations[swapped], locations[fish] \
                    = locations[fish], locations[swapped]
            else:
                locations[fish] = (next_ridx, next_cidx)
            directions[fish] = next_dir
            board[cur_ridx][cur_cidx] = swapped
            board[next_ridx][next_cidx] = fish
            is_moved = True

    return directions, locations, board


def move(eaten: int,
         directions: Directions,
         locations: Locations,
         board: Board) -> int:
    for fish in range(1, 17):
        if locations[fish] != EMPTY:
            directions, locations, board \
                = move_fish(fish, directions, locations, board)

    max_eaten = eaten
    for dist in range(1, 4):
        cur_ridx, cur_cidx = locations[0]
        next_ridx = cur_ridx + dist * move_row[directions[0]]
        next_cidx = cur_cidx + dist * move_col[directions[0]]
        if is_range(next_ridx, next_cidx) \
           and board[next_ridx][next_cidx] != -1:
            new_dirs = copy.deepcopy(directions)
            new_locs = copy.deepcopy(locations)
            new_board = copy.deepcopy(board)

            eaten_fish = board[next_ridx][next_cidx]
            new_eaten = eaten + eaten_fish
            new_dirs[0] = directions[eaten_fish]
            new_locs[0] = new_locs[eaten_fish]
            new_locs[eaten_fish] = EMPTY
            new_board[next_ridx][next_cidx] = -1

            max_eaten = max(max_eaten,
                            move(new_eaten, new_dirs, new_locs, new_board))

    return max_eaten


def main() -> None:
    directions: Directions = [0 for _ in range(17)]
    locations: Locations = [(0, 0) for _ in range(17)]
    board: Board = [[0]*4 for _ in range(4)]

    for ridx in range(4):
        row = list(map(int, input().split()))
        for cidx in range(4):
            fish_num, fish_dir = row[2*cidx], row[2*cidx + 1]
            board[ridx][cidx] = fish_num
            directions[fish_num] = fish_dir - 1
            locations[fish_num] = (ridx, cidx)

    eaten, board[0][0] = board[0][0], -1
    directions[0] = directions[eaten]
    locations[eaten] = EMPTY
    print(move(eaten, directions, locations, board))


if __name__ == "__main__":
    main()
