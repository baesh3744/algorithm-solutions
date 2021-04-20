from typing import List


def list_to_str(num_as_list: List[int]) -> str:
    num_as_str_list: List[str] = [str(value) for value in num_as_list]
    return ''.join(num_as_str_list)


def get_erased(n: int, k: int, num_as_list: List[int]) -> str:
    erased: List[int] = []
    count: int = k

    for num in num_as_list:
        while 0 < len(erased) and 0 < count and erased[-1] < num:
            erased.pop()
            count -= 1
        erased.append(num)

    return list_to_str(erased[:n-k])


def main() -> None:
    n, k = map(int, input().split())
    num_as_list = [int(ch) for ch in input()]

    print(get_erased(n, k, num_as_list))


if __name__ == "__main__":
    main()
