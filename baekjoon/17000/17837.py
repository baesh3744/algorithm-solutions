from typing import TypeVar


T = TypeVar('T', int, list[int])
Location = tuple[int, int]
Board = list[list[T]]

move_loc: list[Location] = [(0, 1), (0, -1), (-1, 0), (1, 0)]
move_dir: list[int] = [1, 0, 3, 2]


class Horse:
    def __init__(self, num: int, loc: Location, dir: int) -> None:
        self.num = num
        self.loc = loc
        self.dir = dir

    def set_loc(self, new_loc: Location) -> None:
        self.loc = new_loc

    def set_dir(self, new_dir: int) -> None:
        self.dir = new_dir


def get_next_loc(loc: Location, dir: int) -> Location:
    return Location(map(sum, zip(loc, move_loc[dir])))


def count_turn(n: int,
               board: Board[int],
               horses: list[Horse],
               horse_board: Board[list[int]]) -> int:
    for turn in range(1, 1001):
        for horse in horses:
            # 이동하려는 칸을 구한다.
            next_x, next_y = get_next_loc(horse.loc, horse.dir)

            # 이동하려는 칸이 파란색인 경우 A를 이동시킨다.
            if (not (0 <= next_x < n and 0 <= next_y < n) or
                    board[next_x][next_y] == 2):
                next_dir = move_dir[horse.dir]
                next_x, next_y = get_next_loc(horse.loc, next_dir)

                horses[horse.num].set_dir(next_dir)

                if (not (0 <= next_x < n and 0 <= next_y < n) or
                        board[next_x][next_y] == 2):
                    continue

            # 이동하려는 말 A와 위에 쌓여있는 말들을 구하고
            # horse_board에서 구한 말들을 제거한다.
            (cur_x, cur_y) = horse.loc
            horse_list = horse_board[cur_x][cur_y]
            height = horse_list.index(horse.num)
            upper_horses = horse_list[height:]
            horse_board[cur_x][cur_y] = horse_list[:height]

            # horse_board에 이동 후 말들의 위치를 표시한다.
            if board[next_x][next_y] == 1:
                upper_horses = list(reversed(upper_horses))
            horse_board[next_x][next_y].extend(upper_horses)

            # A 위에 쌓여있는 말들의 위치를 수정한다.
            for uhorse in upper_horses:
                horses[uhorse].set_loc((next_x, next_y))

            # 말들이 4마리 이상 쌓이면 종료한다.
            if len(horse_board[next_x][next_y]) >= 4:
                return turn

    # 1,000번이 지나도 종료되지 않으면 -1을 리턴한다.
    return -1


def main() -> None:
    n, k = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(n)]

    horses: list[Horse] = []
    horse_board: Board[list[int]] = [[[] for _ in range(n)] for _ in range(n)]
    for hnum in range(k):
        x, y, dir = map(int, input().split())
        horse_board[x - 1][y - 1].append(hnum)
        horses.append(Horse(hnum, (x - 1, y - 1), dir - 1))

    print(count_turn(n, board, horses, horse_board))


if __name__ == "__main__":
    main()
