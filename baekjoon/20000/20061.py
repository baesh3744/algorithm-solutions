import sys


new_row = [0] * 4


class Board:
    def __init__(self) -> None:
        self.board = [[0 for _ in range(4)] for _ in range(6)]
        self.score = 0

    def check_light_block(self) -> None:
        if sum(self.board[0]) > 0:
            for ridx in range(5, 1, -1):
                self.board[ridx] = self.board[ridx - 2]
            self.board[1] = list(new_row)
            self.board[0] = list(new_row)
        elif sum(self.board[1]) > 0:
            for ridx in range(5, 0, -1):
                self.board[ridx] = self.board[ridx - 1]
            self.board[0] = list(new_row)

    def check_row(self, ridx: int) -> None:
        if sum(self.board[ridx]) == 4:
            self.score += 1
            for idx in range(ridx, 0, -1):
                self.board[idx] = self.board[idx - 1]
            self.board[0] = list(new_row)

    def get_top_index(self, y: int) -> int:
        ridx = 0
        while ridx <= 5 and self.board[ridx][y] == 0:
            ridx += 1
        return ridx - 1

    def move_block1(self, y: int) -> None:
        ridx = self.get_top_index(y)
        self.board[ridx][y] = 1
        self.check_row(ridx)
        self.check_light_block()

    def move_block2(self, y: int) -> None:
        ridx = min(self.get_top_index(y), self.get_top_index(y+1))
        self.board[ridx][y] = 1
        self.board[ridx][y+1] = 1
        self.check_row(ridx)
        self.check_light_block()

    def move_block3(self, y: int) -> None:
        ridx = self.get_top_index(y)
        self.board[ridx-1][y] = 1
        self.board[ridx][y] = 1
        self.check_row(ridx - 1)
        self.check_row(ridx)
        self.check_light_block()

    def count_tile(self) -> int:
        return sum(map(lambda x: sum(x), self.board))


def main() -> None:
    blue_board = Board()
    green_board = Board()

    n = int(input())
    for _ in range(n):
        t, x, y = map(int, sys.stdin.readline().split())
        if t == 1:
            blue_board.move_block1(x)
            green_board.move_block1(y)
        elif t == 2:
            blue_board.move_block3(x)
            green_board.move_block2(y)
        else:
            blue_board.move_block2(x)
            green_board.move_block3(y)

    print(blue_board.score + green_board.score)
    print(blue_board.count_tile() + green_board.count_tile())


if __name__ == "__main__":
    main()
