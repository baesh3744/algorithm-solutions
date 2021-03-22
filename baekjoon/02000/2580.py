from typing import List
import copy


def initialize_possible_numbers() -> None:
    global possible_row, possible_col, possible_box
    possible_row = [[num for num in range(1, 10)] for _ in range(1, 10)]
    possible_col = copy.deepcopy(possible_row)
    possible_box = copy.deepcopy(possible_row)

    for ridx in range(9):
        for cidx in range(9):
            value: int = board[ridx][cidx]
            bidx: int = ridx // 3 * 3 + cidx // 3

            if value in possible_row[ridx]:
                possible_row[ridx].remove(value)
            if value in possible_col[cidx]:
                possible_col[cidx].remove(value)
            if value in possible_box[bidx]:
                possible_box[bidx].remove(value)


def solve() -> bool:
    is_finished: bool = False
    for ridx, row in enumerate(board):
        for cidx, number in enumerate(row):
            if number != 0:
                continue

            bidx: int = ridx // 3 * 3 + cidx // 3
            possible: List[int] = []
            for num in possible_row[ridx]:
                if num in possible_col[cidx] and num in possible_box[bidx]:
                    possible.append(num)

            # 넣을 숫자가 없으면 False
            if len(possible) == 0:
                return False

            # 숫자 하나씩 넣어보기
            for num in possible:
                board[ridx][cidx] = num
                possible_row[ridx].remove(num)
                possible_col[cidx].remove(num)
                possible_box[bidx].remove(num)

                is_finished = solve()
                # 스도쿠를 다 채우면 마지막 solve()부터 차례로 True
                if is_finished:
                    return True

                board[ridx][cidx] = 0
                possible_row[ridx].append(num)
                possible_col[cidx].append(num)
                possible_box[bidx].append(num)

            # 숫자를 다 넣어봐도 스도쿠를 다 채울 수 없으면 False
            return False
    return True


def print_board() -> None:
    for row in board:
        for number in row:
            print(number, end=' ')
        print()


def main() -> None:
    global board
    board = [list(map(int, input().split())) for _ in range(9)]

    initialize_possible_numbers()
    solve()
    print_board()


if __name__ == "__main__":
    main()
