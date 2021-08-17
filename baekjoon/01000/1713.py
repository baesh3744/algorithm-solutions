import sys


MAX: int = sys.maxsize


def find(student_list: list[int], info_list: list[list[int]]) -> int:
    min_: list[int] = [MAX, MAX]
    min_index: int = MAX
    for index, student in enumerate(student_list):
        if info_list[student] < min_:
            min_ = info_list[student]
            min_index = index
    return min_index


def get_final_student_list(n: int, recommendation_list: list[int]) -> list[int]:
    order: int = 1
    student_list: list[int] = []
    info_list: list[list[int]] = [[0, 0] for _ in range(101)]
    for student in recommendation_list:
        if info_list[student][0] != 0:
            info_list[student][0] += 1
        else:
            if len(student_list) == n:
                removed = student_list.pop(find(student_list, info_list))
                info_list[removed][0] = 0
            student_list.append(student)
            info_list[student] = [1, order]
            order += 1
    return sorted(student_list)


def main() -> None:
    n = int(input())
    _ = int(input())
    recommendation_list = list(map(int, input().split()))

    print(" ".join(map(str, get_final_student_list(n, recommendation_list))))


if __name__ == "__main__":
    main()
