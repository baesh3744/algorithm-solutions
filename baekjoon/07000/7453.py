from typing import List


def get_pair_count(list1: List[int], list2: List[int]) -> int:
    count: int = 0
    idx1: int = 0
    idx2: int = len(list2) - 1

    while idx1 < len(list1) and 0 <= idx2:
        sub_sum: int = list1[idx1] + list2[idx2]
        if sub_sum == 0:
            count1: int = 0
            while idx1 + count1 < len(list1) and list1[idx1] == list1[idx1 + count1]:
                count1 += 1
            count2: int = 0
            while 0 <= idx2 - count2 and list2[idx2] == list2[idx2 - count2]:
                count2 += 1
            count += count1 * count2
            idx1 += count1
            idx2 += count2
        elif sub_sum < 0:
            idx1 += 1
        else:
            idx2 -= 1

    return count


def get_additions(list1: List[int], list2: List[int]) -> List[int]:
    additions: List[int] = []
    for idx1 in range(len(list1)):
        for idx2 in range(len(list2)):
            additions.append(list1[idx1] + list2[idx2])
    return sorted(additions)


def main() -> None:
    n = int(input())
    list1: List[int] = []
    list2: List[int] = []
    list3: List[int] = []
    list4: List[int] = []
    for _ in range(n):
        a, b, c, d = map(int, input().split())
        list1.append(a)
        list2.append(b)
        list3.append(c)
        list4.append(d)

    print(get_pair_count(get_additions(list1, list2), get_additions(list3, list4)))


if __name__ == "__main__":
    main()
