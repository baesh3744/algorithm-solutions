Elements = dict[int, bool]


def is_friends(x: str, y: str) -> bool:
    return True if set(x) == set(y) else False


def is_almost_friends(data: str, other: str) -> bool:
    minus_chr = {str(num): str(num - 1) for num in range(1, 10)}
    plus_chr = {str(num): str(num + 1) for num in range(9)}
    length: int = len(data)

    for idx in range(length - 1):
        if data[idx] != '0' and data[idx + 1] != '9':
            data_list = list(data)
            data_list[idx] = minus_chr[data_list[idx]]
            data_list[idx + 1] = plus_chr[data_list[idx + 1]]
            if data_list[0] != '0' and is_friends(''.join(data_list), other):
                return True

        if data[idx] != '9' and data[idx + 1] != '0':
            data_list = list(data)
            data_list[idx] = plus_chr[data_list[idx]]
            data_list[idx + 1] = minus_chr[data_list[idx + 1]]
            if data_list[0] != '0' and is_friends(''.join(data_list), other):
                return True
    return False


def get_relationship(x: str, y: str) -> str:
    if is_friends(x, y):
        return 'friends'
    if is_almost_friends(x, y) or is_almost_friends(y, x):
        return 'almost friends'
    return 'nothing'


def main() -> None:
    for _ in range(3):
        x, y = input().split()
        print(get_relationship(x, y))


if __name__ == "__main__":
    main()
