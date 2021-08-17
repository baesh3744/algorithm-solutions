def get_pi(pattern: str) -> list[int]:
    pi: list[int] = [0 for _ in range(len(pattern))]
    prefix_index: int = 0
    for index, char in enumerate(pattern[1:], 1):
        while prefix_index > 0 and char != pattern[prefix_index]:
            prefix_index = pi[prefix_index - 1]
        if char == pattern[prefix_index]:
            prefix_index += 1
            pi[index] = prefix_index
    return pi


def kmp(text: str, pattern: str) -> list[int]:
    pi = get_pi(pattern)
    pattern_index, pattern_length = 0, len(pattern)
    start_list: list[int] = []
    for index, char in enumerate(text):
        while pattern_index > 0 and char != pattern[pattern_index]:
            pattern_index = pi[pattern_index - 1]
        if char == pattern[pattern_index]:
            if pattern_index == pattern_length - 1:
                start_list.append(index - pattern_index + 1)
                pattern_index = pi[pattern_index]
            else:
                pattern_index += 1
    return start_list


def main() -> None:
    t = input()
    p = input()

    start_list = kmp(t, p)
    print(len(start_list))
    for start in start_list:
        print(start)


if __name__ == "__main__":
    main()
