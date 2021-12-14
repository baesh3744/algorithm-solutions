import sys


input = sys.stdin.readline


def getpi(string: str) -> list[int]:
    pi: list[int] = [0 for _ in range(len(string))]
    prefix: int = 0
    for idx, char in enumerate(string[1:], 1):
        while prefix > 0 and char != string[prefix]:
            prefix = pi[prefix - 1]
        if char == string[prefix]:
            prefix += 1
            pi[idx] = prefix
    return pi


if __name__ == "__main__":
    l = int(input())
    string = input().strip()

    pi = getpi(string)
    print(len(string) - pi[-1])
