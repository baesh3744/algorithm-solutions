from typing import List


def get_suffix_array() -> List[int]:
    t: int = 1
    length: int = len(string)
    suffix_array: List[int] = [idx for idx in range(length)]
    group_list: List[int] = [0 for _ in range(length + 1)]

    for idx, char in enumerate(string):
        group_list[idx] = ord(char)

    while t < length:
        suffix_array.sort(key=lambda x: (group_list[x], group_list[min(x + t, length)]))

        ngroup_list: List[int] = [0 for _ in range(length + 1)]
        ngroup_list[suffix_array[0]] = 0
        ngroup_list[-1] = -1

        for idx in range(1, length):
            left, right = suffix_array[idx - 1], suffix_array[idx]
            ngroup_list[right] = ngroup_list[left]
            if (
                group_list[left] != group_list[right]
                or group_list[min(left + t, length)]
                != group_list[min(right + t, length)]
            ):
                ngroup_list[right] += 1

        group_list = ngroup_list[:]
        t <<= 1

    return suffix_array


def get_lcp_array() -> List[int]:
    string_length: int = len(string)
    prefix_length: int = 0
    lcp_array: List[int] = [0 for _ in range(string_length)]
    rank_list: List[int] = [0 for _ in range(string_length)]

    for idx, suffix in enumerate(suffix_array):
        rank_list[suffix] = idx

    for idx, rank in enumerate(rank_list):
        if rank == 0:
            continue

        jdx: int = suffix_array[rank - 1]

        while (
            idx + prefix_length < string_length
            and jdx + prefix_length < string_length
            and string[idx + prefix_length] == string[jdx + prefix_length]
        ):
            prefix_length += 1

        lcp_array[rank] = prefix_length

        if prefix_length > 0:
            prefix_length -= 1

    return lcp_array


if __name__ == "__main__":
    string = input()

    suffix_array = get_suffix_array()
    lcp_array = get_lcp_array()
    print(" ".join(map(lambda x: str(x + 1), suffix_array)))
    print("x " + " ".join(map(str, lcp_array[1:])))
