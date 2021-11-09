import sys


input = sys.stdin.readline


def list_can_check() -> set[int]:
    can_check: set[int] = set([0])

    for choo in choo_list:
        tmp: set[int] = set()
        for check in can_check:
            tmp.update([choo, check + choo, check - choo, choo - check])
        can_check.update(tmp)

    return can_check


if __name__ == "__main__":
    _ = int(input())
    choo_list = list(map(int, input().split()))
    _ = int(input())
    weight_list = map(int, input().split())

    can_check = list_can_check()
    answer = ["Y" if weight in can_check else "N" for weight in weight_list]
    print(" ".join(answer))
