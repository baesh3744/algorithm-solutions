OPERATIONS: set[str] = set(["*", "/", "+", "-"])
PRIORITIES: dict[str, int] = {"*": 0, "/": 0, "+": 1, "-": 1, "(": 2, ")": 2}


def to_postfix(infix: str) -> str:
    ret: str = ""
    stack: list[str] = []
    for char in infix:
        if char.isalpha():
            ret += char
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and (top := stack.pop()) != "(":
                ret += top
        else:
            while stack and PRIORITIES[stack[-1]] <= PRIORITIES[char]:
                ret += stack.pop()
            stack.append(char)
    while stack:
        ret += stack.pop()
    return "".join(ret)


def main() -> None:
    infix = input()
    print(to_postfix(infix))


if __name__ == "__main__":
    main()
