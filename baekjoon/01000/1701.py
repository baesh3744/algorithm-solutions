def get_longest_pattern_length(string: str) -> int:
    pi = [0 for _ in range(len(string))]
    pindex = 0
    for index, char in enumerate(string[1:], 1):
        while pindex > 0 and char != string[pindex]:
            pindex = pi[pindex - 1]
        if char == string[pindex]:
            pindex += 1
            pi[index] = pindex
    return max(pi)


def get_longest_length(string: str) -> int:
    max_ = 0
    for start_index in range(len(string)):
        max_ = max(max_, get_longest_pattern_length(string[start_index:]))
    return max_


def main() -> None:
    string = input()
    print(get_longest_length(string))


if __name__ == "__main__":
    main()
