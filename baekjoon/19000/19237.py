BoardType = list[list[tuple[int, int]]]

EMPTY = (0, 0)
MOVE_X: list[int] = [0, -1, 1, 0, 0]
MOVE_Y: list[int] = [0, 0, 0, -1, 1]


class Shark:
    def __init__(self, num: int) -> None:
        self.num = num
        self.ridx = -1
        self.cidx = -1
        self.dir = -1
        self.priorities: list[list[int]] = [[]]

    def set_location(self, ridx: int, cidx: int) -> None:
        self.ridx = ridx
        self.cidx = cidx

    def set_direction(self, dir: int) -> None:
        self.dir = dir

    def set_priorities(self, priorities: list[list[int]]) -> None:
        self.priorities = priorities

    def get_next_locations(self) -> list[tuple[int, int, int]]:
        nlocations: list[tuple[int, int, int]] = []
        for dir in self.priorities[self.dir-1]:
            nlocations.append(
                (dir, self.ridx+MOVE_X[dir], self.cidx+MOVE_Y[dir]))
        return nlocations


class Board:
    def __init__(self,
                 n: int,
                 m: int,
                 k: int,
                 input_board: list[list[int]]) -> None:
        self.n = n
        self.m = m
        self.k = k
        self.cnt_shark = m
        self.sharks = [Shark(num) for num in range(1, m+1)]
        self.__make_board(input_board)

    def __make_board(self, input_board: list[list[int]]) -> None:
        self.board: BoardType = [[EMPTY]*self.n for _ in range(self.n)]
        for ridx, row in enumerate(input_board):
            for cidx, elem in enumerate(row):
                if elem != 0:
                    self.board[ridx][cidx] = (elem, self.k)
                    self.sharks[elem-1].set_location(ridx, cidx)

    def __is_range(self, ridx: int, cidx: int) -> bool:
        return 0 <= ridx < self.n and 0 <= cidx < self.n

    def get_next_locations(self) -> list[tuple[int, int, int]]:
        next_locations: list[tuple[int, int, int]] \
            = [(-1, -1, -1) for _ in range(self.m)]

        for idx, shark in enumerate(self.sharks):
            if shark.ridx == -1:
                continue

            shark_next_locs = shark.get_next_locations()
            min_priority: int = 2

            for next_dir, next_ridx, next_cidx in shark_next_locs:
                if not self.__is_range(next_ridx, next_cidx):
                    continue

                shark_num, _ = self.board[next_ridx][next_cidx]
                priority = 2

                if shark_num == 0:
                    priority = 0
                elif shark_num == shark.num:
                    priority = 1

                if priority < min_priority:
                    min_priority = priority
                    next_locations[idx] = (next_dir, next_ridx, next_cidx)

        return next_locations

    def pass_one_second(self) -> None:
        for ridx, row in enumerate(self.board):
            for cidx, elem in enumerate(row):
                if elem == EMPTY:
                    continue
                shark, time = elem
                if time == 1:
                    self.board[ridx][cidx] = EMPTY
                else:
                    self.board[ridx][cidx] = (shark, time-1)

    def move(self, next_locations: list[tuple[int, int, int]]) -> None:
        for idx, (shark, loc) in enumerate(zip(self.sharks, next_locations)):
            next_dir, next_ridx, next_cidx = loc
            if next_ridx == -1:
                continue

            shark_num, _ = self.board[next_ridx][next_cidx]
            if shark_num != 0 and shark_num != shark.num:
                if shark.ridx != -1:
                    self.sharks[idx].ridx = -1
                    self.cnt_shark -= 1
                continue

            self.board[next_ridx][next_cidx] = (shark.num, self.k)
            self.sharks[idx].ridx = next_ridx
            self.sharks[idx].cidx = next_cidx
            self.sharks[idx].dir = next_dir


def get_time(board: Board) -> int:
    for time in range(1, 1001):
        next_locations = board.get_next_locations()
        board.pass_one_second()
        board.move(next_locations)
        if board.cnt_shark == 1:
            return time
    return -1


def main() -> None:
    n, m, k = map(int, input().split())
    input_board = [list(map(int, input().split())) for _ in range(n)]

    board = Board(n, m, k, input_board)

    directions = list(map(int, input().split()))
    for idx, dir in enumerate(directions):
        board.sharks[idx].set_direction(dir)

    for idx in range(m):
        priorities = [list(map(int, input().split())) for _ in range(4)]
        board.sharks[idx].set_priorities(priorities)

    print(get_time(board))


if __name__ == "__main__":
    main()
