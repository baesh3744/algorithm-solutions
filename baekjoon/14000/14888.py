from typing import List

MAX: int = -100000001
MIN: int = 100000001
max: int = MAX
min: int = MIN


def operate(operator_index: int, left: int, right: int) -> int:
    if operator_index == 0:
        return left + right
    elif operator_index == 1:
        return left - right
    elif operator_index == 2:
        return left * right
    else:
        if left < 0:
            return ((-1 * left) // right) * -1
        else:
            return left // right


def solve(A: List[int], operators: List[int]) -> None:
    is_finished: bool = True
    for index, operator in enumerate(operators):
        if operator == 0:
            continue

        is_finished = False
        new_A: List[int] = A[:]
        new_A[1] = operate(index, new_A[0], new_A[1])
        new_operators: List[int] = operators[:]
        new_operators[index] -= 1
        solve(new_A[1:], new_operators)

    global max, min
    if is_finished:
        max = max if A[0] < max else A[0]
        min = min if A[0] > min else A[0]


def main() -> None:
    int(input())
    A = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    solve(A, operators)
    print(max if max != MAX else min)
    print(min if min != MIN else max)


if __name__ == "__main__":
    main()
