def find(string: str, start: int) -> tuple[bool, int]:
    index, length = 0, len(string)
    while index < length:
        next_index = index + len(str(start))
        if next_index > length or int(string[index:next_index]) != start:
            return False, -1
        index = next_index
        start += 1
    return True, start - 1


def main() -> None:
    string = input()

    for length in range(1, 4):
        start = int(string[:length])
        is_found, end = find(string, start)
        if is_found:
            print(start, end)
            break


if __name__ == "__main__":
    main()
