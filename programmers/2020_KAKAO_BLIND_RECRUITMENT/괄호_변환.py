from typing import Tuple


OPEN: str = "("
CLOSE: str = ")"


def split(string: str) -> Tuple[str, str]:
    balance, index = 0, 0
    for idx, char in enumerate(string):
        balance += 1 if char == OPEN else -1
        if balance == 0:
            index = idx + 1
            break
    return string[:index], string[index:]


def is_right_parenthesis_string(string: str) -> bool:
    stack: int = 0
    for char in string:
        stack += 1 if char == OPEN else -1
        if stack < 0:
            return False
    return True


def reverse(string: str) -> str:
    return "".join([OPEN if char == CLOSE else CLOSE for char in string])


def solution(p: str) -> str:
    if not p or is_right_parenthesis_string(p):
        return p
    u, v = split(p)
    if is_right_parenthesis_string(u):
        return u + solution(v)
    return OPEN + solution(v) + CLOSE + reverse(u[1:-1])


# "(()())()"
print(solution("(()())()"))
# "()"
print(solution(")("))
# "()(())()"
print(solution("()))((()"))
# ""
print(solution(""))
