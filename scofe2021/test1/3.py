from typing import List


def count(N: int, size: int) -> int:
    num: int = 0
    for row in range(N):
        for col in range(N):
            if not possible[row][col] or N <= row + size - 1 or N <= col + size - 1:
                continue

            is_collocated: bool = True
            for move_row in range(size):
                if not is_collocated:
                    break

                for move_col in range(size):
                    if space[row + move_row][col + move_col] == 0:
                        is_collocated = False
                        possible[row][col] = False
                        break
            if is_collocated:
                num += 1
    return num


def get_answer(N: int) -> List[int]:
    answer: List[int] = []
    total: int = 0
    for size in range(1, N + 1):
        num: int = count(N, size)
        if num == 0:
            break
        answer.append(num)
        total += num
    answer.insert(0, total)
    return answer


def print_answer(answer: List[int]) -> None:
    for index, ans in enumerate(answer):
        if index == 0:
            print('total: {}'.format(ans))
        else:
            print('size[{}]: {}'.format(index, ans))


def main() -> None:
    global space, possible
    N = int(input())
    space = [[int(ch) for ch in input()] for _ in range(N)]

    possible = [[True for _ in range(N)] for _ in range(N)]

    answer: List[int] = get_answer(N)

    print_answer(answer)


if __name__ == "__main__":
    main()
