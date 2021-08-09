def count_alphabet(target_length: int, string: str) -> int:
    used = {chr(ascii_): 0 for ascii_ in range(97, 123)}
    for char in string[:target_length]:
        used[char] += 1

    cnt_alphabet = sum(cnt > 0 for cnt in used.values())
    for index, char in enumerate(string[target_length:]):
        used[char] += 1
        used[string[index]] -= 1
        cnt_alphabet = min(cnt_alphabet, sum(cnt > 0 for cnt in used.values()))

    return cnt_alphabet


def search(n: int, string: str) -> int:
    left, right = 0, len(string)
    while left <= right:
        mid = (left + right) // 2
        if count_alphabet(mid, string) <= n:
            left = mid + 1
        else:
            right = mid - 1
    return right


def main() -> None:
    n = int(input())
    string = input()

    print(search(n, string))


if __name__ == "__main__":
    main()
