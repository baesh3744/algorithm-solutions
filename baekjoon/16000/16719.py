used: list[bool]


def dfs(string: str, start: int, end: int) -> None:
    if start >= end:
        return

    substring: str = string[start:end]
    index: int = start + substring.index(min(substring))
    used[index] = True

    print("".join(char for char, is_used in zip(string, used) if is_used))
    dfs(string, index + 1, end)
    dfs(string, start, index)


def main() -> None:
    global used
    string = input()

    length: int = len(string)
    used = [False for _ in range(length)]
    dfs(string, 0, length)


if __name__ == "__main__":
    main()
