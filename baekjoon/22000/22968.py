import sys


IMPOSSIBLE: int = -1
MAX: int = 45

input = sys.stdin.readline


def list_v_by_height() -> list[int]:
    vlist: list[int] = [num for num in range(MAX)]
    for index in range(2, MAX):
        vlist[index] = vlist[index - 1] + vlist[index - 2]
    for index in range(1, MAX):
        vlist[index] += vlist[index - 1]
    return vlist


def get_height(v: int, vlist: list[int]) -> int:
    for height, (cur_v, next_v) in enumerate(zip(vlist[:-1], vlist[1:])):
        if cur_v <= v < next_v:
            return height
    return IMPOSSIBLE


def main() -> None:
    t = int(input())
    vlist = list_v_by_height()
    for _ in range(t):
        v = int(input())
        print(get_height(v, vlist))


if __name__ == "__main__":
    main()
