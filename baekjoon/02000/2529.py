from typing import List


def find_min(signs: List[str]) -> None:
    ret: List[str] = []
    number: int = 0
    count: int = 0
    for s in signs:
        if s == '>':
            count += 1
        else:
            for c in range(count, -1, -1):
                ret.append(str(number + c))
            number += (count + 1)
            count = 0
    for c in range(count, -1, -1):
        ret.append(str(number + c))
    print(''.join(ret))


def find_max(signs: List[str]) -> None:
    ret: List[str] = []
    number: int = 9
    count: int = 0
    for s in signs:
        if s == '<':
            count += 1
        else:
            for c in range(count, -1, -1):
                ret.append(str(number - c))
            number -= (count + 1)
            count = 0
    for c in range(count, -1, -1):
        ret.append(str(number - c))
    print(''.join(ret))


def main() -> None:
    k: int = int(input())
    signs: List[str] = list(map(str, input().split()))
    find_max(signs)
    find_min(signs)


if __name__ == "__main__":
    main()
