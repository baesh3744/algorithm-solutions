import operator
import sys


MIN = -sys.maxsize

op_dict = {"*": operator.mul, "+": operator.add, "-": operator.sub}


def calculate(left: str, op: str, right: str) -> str:
    return str(op_dict[op](int(left), int(right)))


def calc_max(expression_list: list[str]) -> str:
    length: int = len(expression_list)
    if length == 1:
        return expression_list[0]

    expression: str = "".join(expression_list)
    if expression in cache:
        return cache[expression]

    max_result: int = MIN

    for idx in range(0, length - 2, 2):
        calculated: str = calculate(*expression_list[idx : idx + 3])
        new_expression_list: list[str] = (
            expression_list[:idx] + [calculated] + expression_list[idx + 3 :]
        )
        max_result = max(max_result, int(calc_max(new_expression_list)))

    cache[expression] = str(max_result)
    return cache[expression]


if __name__ == "__main__":
    n = int(input())
    expression_list = list(input().strip())

    cache: dict[str, str] = dict()
    print(calc_max(expression_list))
