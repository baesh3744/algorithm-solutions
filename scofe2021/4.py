from typing import Any, List


def parse_contents(status_input: List[str], genres_input: List[str], preference: List[float]) -> List[List[Any]]:
    contents: List[List[Any]] = []
    for row, status_row in enumerate(status_input):
        for col, status in enumerate(status_row):
            if status == 'W':
                continue

            genre = genres_input[row][col]
            contents.append(
                [status, preference[ord(genre) - ord('A')], genre, row, col])
    return contents


def compare(left: List[Any], right: List[Any]) -> int:
    if left[0] == 'O' and right[0] == 'Y':
        return 1
    elif left[0] == 'Y' and right[0] == 'O':
        return -1
    else:
        if left[1] < right[1]:
            return 1
        elif left[1] > right[1]:
            return -1
        else:
            if left[3] > right[3] or (left[3] == right[3] and left[4] > right[4]):
                return 1
            elif left[3] < right[3] or (left[3] == right[3] and left[4] < right[4]):
                return -1
    return 0


def quick_sort(array: List[List[Any]]) -> List[List[Any]]:
    if len(array) <= 1:
        return array

    pivot: List[Any] = array[len(array) // 2]
    left_array: List[List[Any]] = []
    right_array: List[List[Any]] = []
    for item in array:
        switch: int = compare(item, pivot)
        if switch == 1:
            right_array.append(item)
        elif switch == -1:
            left_array.append(item)
    return quick_sort(left_array) + [pivot] + quick_sort(right_array)


def print_contents(sorted_contents: List[List[Any]]) -> None:
    for contents in sorted_contents:
        print('{} {} {} {}'.format(
            contents[2], contents[1], contents[3], contents[4]))


def main() -> None:
    preference = list(map(float, input().split()))
    N, _ = map(int, input().split())
    status_input = [input() for _ in range(N)]
    genres_input = [input() for _ in range(N)]

    contents = parse_contents(status_input, genres_input, preference)
    sorted_contents: List[List[Any]] = quick_sort(contents)
    print_contents(sorted_contents)


if __name__ == "__main__":
    main()
