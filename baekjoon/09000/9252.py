from typing import List


def make_lcs_table(str1: str, str2: str) -> List[List[int]]:
    lcs_table: List[List[int]] = [
        [0 for _ in range(len(str2))] for _ in range(len(str1))]

    for idx1 in range(1, len(str1)):
        for idx2 in range(1, len(str2)):
            if str1[idx1] == str2[idx2]:
                lcs_table[idx1][idx2] = lcs_table[idx1-1][idx2-1] + 1
            else:
                lcs_table[idx1][idx2] = max(lcs_table[idx1-1][idx2],
                                            lcs_table[idx1][idx2-1])

    return lcs_table


def get_lcs(str1: str, str2: str, lcs_length: int, lcs_table: List[List[int]]) -> str:
    lcs: str = ''
    next_idx2: int = len(str2) - 1
    length: int = lcs_length

    for idx1 in range(len(str1)-1, 0, -1):
        for idx2 in range(next_idx2, 0, -1):
            if str1[idx1] == str2[idx2] and lcs_table[idx1][idx2] == length:
                lcs = str1[idx1] + lcs
                next_idx2 = idx2 - 1
                length -= 1
                break

    return lcs


def main() -> None:
    str1 = input()
    str2 = input()

    str1 = '0' + str1
    str2 = '0' + str2

    lcs_table: List[List[int]] = make_lcs_table(str1, str2)
    lcs_length: int = max(lcs_table[len(str1) - 1])
    lcs: str = get_lcs(str1, str2, lcs_length, lcs_table)
    print(lcs_length)
    print(lcs)


if __name__ == "__main__":
    main()
