from typing import List


MAX: int = 1000000000
MIN: int = -1000000000
max: int = MIN
min: int = MAX


def calculate(left: int, right: int, type: int) -> int:
    if type == 0:
        return left + right
    elif type == 1:
        return left - right
    elif type == 2:
        return left * right
    # type == 3
    elif left >= 0:
        return left // right
    else:
        return ((left * -1) // right) * -1


def solve(A: List[int], operators: List[int]) -> None:
    if len(A) == 1:
        global max, min
        max = max if A[0] < max else A[0]
        min = min if A[0] > min else A[0]
        return

    for type, operator in enumerate(operators):
        if operator > 0:
            new_A: List[int] = A[2:]
            new_operators: List[int] = operators[:]

            new_A.insert(0, calculate(A[0], A[1], type))
            new_operators[type] -= 1
            solve(new_A, new_operators)


def main() -> None:
    _ = int(input())
    A = list(map(int, input().split()))
    operators = list(map(int, input().split()))

    solve(A, operators)
    print(max)
    print(min)


if __name__ == "__main__":
    main()
