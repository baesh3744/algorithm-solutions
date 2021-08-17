import sys


input = sys.stdin.readline


def main() -> None:
    n = int(input())
    word_list = [input().strip() for _ in range(n)]

    word_list.sort()

    cnt: int = len(word_list)
    for index, word in enumerate(word_list):
        if index > 0 and word.startswith(word_list[index - 1]):
            cnt -= 1
    print(cnt)


if __name__ == "__main__":
    main()
