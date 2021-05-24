def get_cut_length(trees: list[int], height: int) -> int:
    cut_length: int = 0
    for tree in trees:
        if (cut := tree - height) > 0:
            cut_length += cut
    return cut_length


def get_max_height(m: int, trees: list[int]) -> int:
    left: int = 0
    right: int = max(trees)

    while left <= right:
        mid: int = (left + right) // 2

        cut_length = get_cut_length(trees, mid)

        if cut_length >= m:
            left = mid + 1
        else:
            right = mid - 1

    return right


def main() -> None:
    _, m = map(int, input().split())
    trees = list(map(int, input().split()))

    print(get_max_height(m, trees))


if __name__ == "__main__":
    main()
