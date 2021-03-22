from typing import List


inputs: List[int]
checked: List[bool]


def print_list() -> None:
    for index, is_checked in enumerate(checked):
        if is_checked:
            print(inputs[index + 1], end=' ')
    print('')


def back_tracking(count: int, current: int) -> None:
    global checked
    if count == 6:
        print_list()
        return

    for next in range(current, len(checked)):
        if count < 6:
            checked[next] = True
            back_tracking(count + 1, next + 1)
            checked[next] = False


def main() -> None:
    while True:
        global inputs, checked
        inputs = list(map(int, input().split()))

        if inputs[0] == 0:
            return

        checked = [False for _ in range(inputs[0])]
        back_tracking(0, 0)
        print('')


if __name__ == "__main__":
    main()
