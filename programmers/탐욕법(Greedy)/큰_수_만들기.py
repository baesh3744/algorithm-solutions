from collections import deque


def solution(number: str, k: int) -> str:
    stack: deque[str] = deque()
    for num in number:
        while 0 < k and stack and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    while k:
        stack.pop()
        k -= 1
    return ''.join(stack)


# "94"
print(solution("1924", 2))
# "3234"
print(solution("1231234", 3))
# "775841"
print(solution("4177252841", 4))
# "100"
print(solution("1000", 1))
